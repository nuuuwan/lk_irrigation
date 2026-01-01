# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_19:19:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 19:19:17 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.008 |  |
| 2026-01-01 19:10:32 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:09:05 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:08:16 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 19:07:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-01-01 19:07:17 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:06:36 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:06:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 19:06:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:06:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.039 |  |
| 2026-01-01 19:05:59 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-01-01 19:05:56 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:50 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-01 19:05:38 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.108 |  |
| 2026-01-01 19:05:35 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:33 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 19:05:25 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 19:04:28 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 19:04:18 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:04:07 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-01-01 19:03:46 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-01-01 19:03:36 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:03:23 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:02:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-01-01 19:02:44 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:02:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:02:13 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-01-01 19:01:57 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:01:43 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:01:22 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:01:21 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-01 19:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-01 19:01:04 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:00:34 | Horowpothana (Yan Oya) | 3.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 18:59:47 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-01 18:27:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 19:01:21 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-01 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 19:05:50 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-01 18:59:47 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-01 19:00:34 | Horowpothana (Yan Oya) | 3.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 19:08:16 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 19:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-01 19:06:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 19:04:28 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 19:05:25 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 19:09:05 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:03:23 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:06:36 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:01:57 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:06:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:35 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:01:04 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:33 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:02:44 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:05:56 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:10:32 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:07:17 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 19:19:17 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.008 |  |
| 2026-01-01 19:04:18 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:03:36 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:01:22 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:02:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.010 |  |
| 2026-01-01 19:02:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-01-01 19:07:24 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-01-01 19:05:59 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 19:02:13 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-01-01 19:04:07 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-01-01 19:06:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.039 |  |
| 2026-01-01 19:03:46 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-01 18:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-01-01 19:05:38 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)