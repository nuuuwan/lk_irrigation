# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_04:18:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 04:18:43 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-15 04:17:26 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:14:28 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:13:49 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-15 04:11:18 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:10:14 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-15 04:10:13 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-15 04:05:52 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -180.000 |  |
| 2026-01-15 04:05:51 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -180.000 |  |
| 2026-01-15 04:05:50 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -180.000 |  |
| 2026-01-15 04:05:37 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-15 04:05:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.057 |  |
| 2026-01-15 04:04:55 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:04:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:04:16 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:03:56 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.050 |  |
| 2026-01-15 04:03:53 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.024 |  |
| 2026-01-15 04:03:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-15 04:03:13 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.169 |  |
| 2026-01-15 04:03:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-15 04:02:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-01-15 04:02:25 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:09 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:06 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:05 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:01:45 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:01:43 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-01-15 04:01:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:01:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:00:51 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.032 |  |
| 2026-01-15 04:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:00:31 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-01-15 04:00:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:00:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:49:53 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-15 03:49:31 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-15 03:49:12 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.025 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 04:10:14 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-15 03:08:02 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-15 04:05:37 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-15 04:18:43 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-15 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 04:13:49 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-15 03:12:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 03:18:27 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-15 04:02:25 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:01:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:11:18 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:06 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:09 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:04:43 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:04:16 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:01:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:05 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:02:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:01:45 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:17:26 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:14:28 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:04:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:04:55 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:00:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:03:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-15 04:02:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-01-15 04:01:43 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 04:03:53 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.024 |  |
| 2026-01-15 04:03:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-15 04:00:51 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.032 |  |
| 2026-01-15 04:00:31 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-01-15 04:03:56 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.050 |  |
| 2026-01-15 04:05:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.057 |  |
| 2026-01-15 04:03:13 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.169 |  |
| 2026-01-15 04:05:52 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)