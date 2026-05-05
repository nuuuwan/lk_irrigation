# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_04:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 04:18:24 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:15:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:15:36 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:15:35 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:13:20 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.035 |  |
| 2026-05-06 04:10:12 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-06 04:08:41 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-06 04:05:58 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-05-06 04:05:52 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 04:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 04:05:17 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-05-06 04:04:27 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:04:09 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:03:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:03:18 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-06 04:03:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:03:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-06 04:02:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.257 |  |
| 2026-05-06 04:02:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:02:38 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:02:26 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:02:23 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:02:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:01:56 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:35 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:20 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.040 |  |
| 2026-05-06 04:00:57 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-05-06 04:00:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-06 04:00:27 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.123 |  |
| 2026-05-06 04:00:18 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-06 04:00:10 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 03:13:27 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-05-06 04:10:12 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-06 04:00:18 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-06 04:00:10 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 04:08:41 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-06 04:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 04:05:52 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 04:02:23 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:35 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:15:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:15:56 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:02:26 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:03:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:04:09 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:02:38 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:04:27 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:04:47 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:18:24 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 04:01:56 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:02:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:03:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:02:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-06 04:05:17 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.012 |  |
| 2026-05-06 04:05:58 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-05-06 04:03:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-05-06 04:03:18 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-06 04:00:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-06 03:05:47 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-05-06 04:13:20 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.035 |  |
| 2026-05-06 04:01:20 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.040 |  |
| 2026-05-06 04:00:57 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-05-06 04:00:27 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.123 |  |
| 2026-05-06 04:02:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)