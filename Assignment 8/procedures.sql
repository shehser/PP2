-- Upsert procedure
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

--  Bulk-insert procedure with phone format validation
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    IN p_names VARCHAR[],
    IN p_phones VARCHAR[],
    OUT p_rejected_records TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    v_name VARCHAR;
    v_phone VARCHAR;
BEGIN
    p_rejected_records := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(p_names, 1) LOOP
        v_name := p_names[i];
        v_phone := p_phones[i];

        -- Validates that the number contains 7 to 15 sequential digits
        IF v_phone SIMILAR TO '[0-9]{7,15}' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = v_name) THEN
                UPDATE contacts SET phone = v_phone WHERE name = v_name;
            ELSE
                INSERT INTO contacts(name, phone) VALUES(v_name, v_phone);
            END IF;
        ELSE
            p_rejected_records := array_append(
                p_rejected_records,
                'Name: ' || v_name || ', Phone: ' || v_phone || ' (Invalid Format)'
            );
        END IF;
    END LOOP;
END;
$$;

--  Delete procedure
CREATE OR REPLACE PROCEDURE delete_contact(p_search_term VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_search_term
       OR phone = p_search_term;
END;
$$;
