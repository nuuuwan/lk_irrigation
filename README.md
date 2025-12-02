# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_14:09:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,491 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 14:09:16 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 1.205 | 🔺 Rising |
| 2025-12-02 14:09:14 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2025-12-02 14:09:11 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | -0.022 |  |
| 2025-12-02 14:07:36 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.062 |  |
| 2025-12-02 14:07:04 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.029 |  |
| 2025-12-02 14:07:01 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:06:07 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-02 14:05:48 | Hanwella (Kelani Ganga) | 7.14 | 🟡 Alert | -0.080 |  |
| 2025-12-02 14:05:00 | Nagalagam Street (Kelani Ganga) | 2.10 | 🟠 Minor Flood | -0.029 |  |
| 2025-12-02 14:04:54 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:04:25 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2025-12-02 14:04:20 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:04:14 | Ellagawa (Kalu Ganga) | 9.62 | 🟢 Normal | -0.070 |  |
| 2025-12-02 14:04:04 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.087 |  |
| 2025-12-02 14:03:50 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-02 14:03:49 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2025-12-02 14:03:30 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-02 14:03:11 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | -0.020 |  |
| 2025-12-02 14:02:54 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.013 |  |
| 2025-12-02 14:02:32 | Horowpothana (Yan Oya) | 4.12 | 🟢 Normal | 1.391 | 🔺 Rising |
| 2025-12-02 14:02:31 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:02:25 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.061 |  |
| 2025-12-02 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:02:05 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:02:02 | Thanthirimale (Malwathu Oya) | 9.24 | 🔴 Major Flood | 0.908 | 🔺 Rising |
| 2025-12-02 14:01:48 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:01:03 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2025-12-02 14:00:54 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2025-12-02 14:00:38 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-02 13:20:19 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-02 13:16:48 | Galgamuwa (Mee Oya) | 3.02 | 🟢 Normal | -0.055 |  |
| 2025-12-02 13:15:48 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.087 |  |
| 2025-12-02 13:15:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:15:29 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 1.205 | 🔺 Rising |
| 2025-12-02 13:15:06 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 1.391 | 🔺 Rising |
| 2025-12-02 13:15:00 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 14:02:02 | Thanthirimale (Malwathu Oya) | 9.24 | 🔴 Major Flood | 0.908 | 🔺 Rising |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 14:05:00 | Nagalagam Street (Kelani Ganga) | 2.10 | 🟠 Minor Flood | -0.029 |  |
| 2025-12-02 14:03:11 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | -0.020 |  |
| 2025-12-02 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.061 |  |
| 2025-12-02 14:05:48 | Hanwella (Kelani Ganga) | 7.14 | 🟡 Alert | -0.080 |  |
| 2025-12-02 14:02:32 | Horowpothana (Yan Oya) | 4.12 | 🟢 Normal | 1.391 | 🔺 Rising |
| 2025-12-02 14:09:16 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 1.205 | 🔺 Rising |
| 2025-12-02 13:03:45 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-02 13:20:19 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-02 14:02:31 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:02:05 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 13:15:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:07:01 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 14:04:54 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:04:20 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:02:25 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:00:38 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:01:48 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-02 14:03:30 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2025-12-02 14:03:49 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 14:02:54 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.013 |  |
| 2025-12-02 14:04:25 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2025-12-02 14:06:07 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-02 14:03:50 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-02 14:01:03 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2025-12-02 14:09:14 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2025-12-02 14:09:11 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | -0.022 |  |
| 2025-12-02 14:07:04 | Glencourse (Kelani Ganga) | 11.32 | 🟢 Normal | -0.029 |  |
| 2025-12-02 14:00:54 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2025-12-02 13:16:48 | Galgamuwa (Mee Oya) | 3.02 | 🟢 Normal | -0.055 |  |
| 2025-12-02 14:07:36 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.062 |  |
| 2025-12-02 14:04:14 | Ellagawa (Kalu Ganga) | 9.62 | 🟢 Normal | -0.070 |  |
| 2025-12-02 14:04:04 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)