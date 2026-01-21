# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_11:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 11:15:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-21 11:12:34 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:10:40 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:10:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:09:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.068 |  |
| 2026-01-21 11:09:22 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:06:00 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:05:21 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.043 |  |
| 2026-01-21 11:05:16 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-21 11:05:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:04:34 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:04:04 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:04:00 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:58 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:56 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:33 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-21 11:03:21 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:15 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-21 11:03:07 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:06 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-01-21 11:03:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:54 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:53 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-21 11:02:38 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 11:02:34 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-21 11:02:22 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:17 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.031 |  |
| 2026-01-21 11:02:11 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:06 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:46 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-01-21 11:01:41 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 11:01:31 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:00:43 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:00:43 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:00:12 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:25:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 11:03:06 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-01-21 11:05:16 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-21 11:15:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-21 11:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 11:02:38 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 11:00:43 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:34 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:12:34 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:00:43 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:46 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:21 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:41 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:10:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:09:22 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:00 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:11 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:17 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:58 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:38 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:22 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:05:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:07 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:10:40 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:06 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:04:00 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:06:00 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:01:31 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:54 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:56 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:04:34 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 11:03:15 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-21 11:02:53 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-21 11:03:33 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-21 11:01:46 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-01-21 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-21 11:02:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.031 |  |
| 2026-01-21 11:05:21 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.043 |  |
| 2026-01-21 11:09:53 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)