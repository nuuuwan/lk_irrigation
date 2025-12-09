# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_19:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 19:13:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:10:10 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-09 19:09:50 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2025-12-09 19:09:33 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-09 19:06:55 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:06:53 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-09 19:06:07 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:06:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:05:25 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 19:05:03 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 19:04:31 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:04:30 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 19:04:21 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:04:14 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2025-12-09 19:04:09 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 19:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-09 19:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-09 19:03:50 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:03:40 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 19:03:36 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.070 |  |
| 2025-12-09 19:02:58 | Urawa (Nilwala Ganga) | 3.33 | 🟡 Alert | 0.415 | 🔺 Rising |
| 2025-12-09 19:02:51 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 19:02:45 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.080 |  |
| 2025-12-09 19:02:05 | Yaka Wewa (Ma Oya) | 1.83 | 🟢 Normal | -0.091 |  |
| 2025-12-09 19:02:05 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.110 |  |
| 2025-12-09 19:01:59 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-09 19:01:58 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:01:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2025-12-09 19:01:37 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 19:00:15 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 19:02:58 | Urawa (Nilwala Ganga) | 3.33 | 🟡 Alert | 0.415 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 19:01:59 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-09 19:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-09 19:09:33 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-09 19:04:30 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 19:05:03 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 18:05:29 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 19:02:51 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 19:01:37 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 19:10:10 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-09 19:06:53 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-09 19:05:25 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 19:04:09 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 19:03:40 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 19:04:21 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:04:31 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:13:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:06:55 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:06:07 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:06:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:03:50 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:01:58 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-09 19:00:15 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 19:09:50 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 19:04:14 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2025-12-09 18:04:38 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.050 |  |
| 2025-12-09 19:01:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2025-12-09 19:03:36 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.070 |  |
| 2025-12-09 19:02:45 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.080 |  |
| 2025-12-09 19:02:05 | Yaka Wewa (Ma Oya) | 1.83 | 🟢 Normal | -0.091 |  |
| 2025-12-09 19:02:05 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)