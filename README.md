# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_12:10:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 12:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-07 12:09:24 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:08:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-07 12:07:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-07 12:07:42 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-07 12:06:21 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-07 12:06:05 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:05:53 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 12:05:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:05:48 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.039 |  |
| 2026-06-07 12:05:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:04:27 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 12:04:19 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 12:04:19 | Rathnapura (Kalu Ganga) | 4.61 | 🟢 Normal | -0.070 |  |
| 2026-06-07 12:04:02 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-06-07 12:03:51 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 12:03:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-07 12:03:32 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-07 12:03:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:03:07 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:54 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.200 |  |
| 2026-06-07 12:02:54 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-06-07 12:02:36 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:33 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:19 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-06-07 12:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:16 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 12:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.031 |  |
| 2026-06-07 12:01:43 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:35 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:30 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 12:01:25 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-07 12:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:16 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:00:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:00:16 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-07 11:30:43 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 12:03:32 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-07 12:07:42 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-07 12:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-07 12:01:30 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 12:04:27 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-07 12:02:16 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 12:06:21 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-07 12:05:53 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 12:07:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-07 12:03:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-07 12:01:25 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-07 12:04:19 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 12:03:51 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 12:08:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-07 12:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:36 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:05:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:03:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:06:05 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:09:24 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:33 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:05:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:35 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:16 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:03:07 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:00:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:01:43 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 12:02:19 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-06-07 12:02:54 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-06-07 12:00:16 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-07 12:04:02 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-06-07 12:01:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.031 |  |
| 2026-06-07 12:05:48 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.039 |  |
| 2026-06-07 12:04:19 | Rathnapura (Kalu Ganga) | 4.61 | 🟢 Normal | -0.070 |  |
| 2026-06-07 12:02:54 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)