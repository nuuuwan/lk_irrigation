# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_06:09:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 06:09:29 | Nagalagam Street (Kelani Ganga) | 1.52 | 🟠 Minor Flood | -0.087 |  |
| 2025-12-03 06:07:33 | Horowpothana (Yan Oya) | 3.25 | 🟢 Normal | -0.029 |  |
| 2025-12-03 06:07:10 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:06:49 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-03 06:05:55 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.048 |  |
| 2025-12-03 06:05:46 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.049 |  |
| 2025-12-03 06:05:38 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-03 06:05:10 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:04:43 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.156 |  |
| 2025-12-03 06:04:35 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-03 06:04:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:04:04 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:03:08 | Thanthirimale (Malwathu Oya) | 7.54 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-03 06:03:04 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:02:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-03 06:02:36 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:02:35 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.082 |  |
| 2025-12-03 06:02:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | -0.030 |  |
| 2025-12-03 06:02:12 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:01:31 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:01:31 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.031 |  |
| 2025-12-03 06:01:17 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.022 |  |
| 2025-12-03 06:01:16 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:01:11 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:01:09 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-03 06:01:06 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | -0.020 |  |
| 2025-12-03 06:00:52 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:38:31 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:11:55 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:11:14 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:10:52 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.156 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-03 06:03:08 | Thanthirimale (Malwathu Oya) | 7.54 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-03 06:09:29 | Nagalagam Street (Kelani Ganga) | 1.52 | 🟠 Minor Flood | -0.087 |  |
| 2025-12-03 06:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | -0.030 |  |
| 2025-12-03 06:01:31 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.031 |  |
| 2025-12-03 06:04:35 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-03 06:05:38 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-03 06:02:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-03 06:01:09 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-03 06:04:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:04:04 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:11:55 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:03:04 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:01:31 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:07:10 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 03:02:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:01:11 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:00:52 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:02:12 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 05:38:31 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:02:36 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-03 06:06:49 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-03 06:05:10 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:01:16 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-03 06:02:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-03 04:11:13 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.012 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 06:01:06 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | -0.020 |  |
| 2025-12-03 06:01:17 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.022 |  |
| 2025-12-03 06:07:33 | Horowpothana (Yan Oya) | 3.25 | 🟢 Normal | -0.029 |  |
| 2025-12-03 06:05:55 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.048 |  |
| 2025-12-03 06:05:46 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.049 |  |
| 2025-12-03 06:02:35 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.082 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 06:04:43 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)