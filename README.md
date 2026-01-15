# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_18:11:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,460 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 18:11:41 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-01-15 18:08:13 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.036 |  |
| 2026-01-15 18:07:33 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |
| 2026-01-15 18:07:03 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-01-15 18:06:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:06:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:06:14 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:06:03 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-01-15 18:05:53 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:05:28 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 18:05:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-01-15 18:04:20 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:04:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:04:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:38 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:23 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 18:03:15 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:02:55 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:02:48 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-15 18:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:02:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.054 |  |
| 2026-01-15 18:02:18 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-15 18:02:12 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-15 18:01:41 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:01:36 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-15 18:01:33 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-01-15 18:01:30 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:26 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:25 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-01-15 18:01:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:00:53 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:00:39 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-15 18:00:27 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:59:19 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:18:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 18:02:48 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-01-15 18:02:12 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-15 18:01:36 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-15 18:03:23 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 18:05:28 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 18:06:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:04:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:00:39 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:00:53 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:25 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:30 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:15 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:02:55 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:26 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:38 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:05:53 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-15 17:02:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:01:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:06:03 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-01-15 18:07:33 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:04:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:01:41 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:06:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:00:27 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:04:20 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-15 17:59:19 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 18:02:18 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-01-15 18:01:33 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-01-15 18:07:03 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.024 |  |
| 2026-01-15 18:05:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-01-15 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-15 18:08:13 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.036 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-15 18:11:41 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-01-15 18:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-01-15 18:02:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.054 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)