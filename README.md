# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_11:14:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 11:14:04 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:11:25 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-29 11:11:06 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:10:21 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:10:08 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:09:21 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-29 11:08:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:07:43 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 11:07:29 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-01-29 11:06:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:06:14 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:48 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:04:28 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:25 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:18 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.043 |  |
| 2026-01-29 11:04:11 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:09 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:03:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 11:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:03:31 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-29 11:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:02:59 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.097 |  |
| 2026-01-29 11:02:58 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:02:55 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.034 |  |
| 2026-01-29 11:02:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-01-29 11:02:18 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-01-29 11:02:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-01-29 11:02:12 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:01:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.240 |  |
| 2026-01-29 11:01:04 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:01:00 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 11:00:40 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:00:37 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:00:18 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:30:47 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 11:09:21 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-29 11:03:31 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-29 11:01:00 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 11:00:18 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 11:03:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 11:07:43 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 11:02:58 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:01:04 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:00:21 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:10:08 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:28 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:06:14 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:09:46 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:11:06 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:02:55 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:07:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:02:12 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:00:37 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:06:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:08:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:25 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:14:04 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:11 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:04:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 11:11:25 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-29 10:11:30 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-29 11:04:09 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:00:40 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:04:48 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-29 11:02:16 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-01-29 11:02:18 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-01-29 11:02:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-01-29 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.034 |  |
| 2026-01-29 11:04:18 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.043 |  |
| 2026-01-29 11:02:59 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.097 |  |
| 2026-01-29 11:07:29 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-01-29 11:01:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)