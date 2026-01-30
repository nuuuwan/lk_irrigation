# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_22:25:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 22:25:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:21:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:13:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:12:42 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:12:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-01-30 22:11:15 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:11:13 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.882 | 🔺 Rising |
| 2026-01-30 22:09:36 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.019 |  |
| 2026-01-30 22:08:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-30 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-30 22:07:57 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-30 22:07:32 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:07:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:06:08 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-01-30 22:06:06 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 22:05:52 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-30 22:05:19 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-30 22:04:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.096 |  |
| 2026-01-30 22:04:24 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:03:54 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-30 22:03:51 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:03:19 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-30 22:02:29 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:23 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:17 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:01:59 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:01:55 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:01:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-30 22:01:39 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:01:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-30 22:00:51 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:50 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:50 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 21:42:05 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 22:08:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-30 22:11:13 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.882 | 🔺 Rising |
| 2026-01-30 22:12:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-01-30 22:03:54 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-30 22:01:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-30 22:05:19 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-30 22:06:06 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 22:08:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:02:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:01:59 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:07:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 22:00:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 21:20:00 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:04:24 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:17 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:51 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:11:15 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:21:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:23 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:01:55 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:13:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 21:02:36 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:50 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:07:32 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:02:29 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 21:08:49 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:00:50 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-30 21:05:36 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:25:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:03:51 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-30 22:05:52 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-30 22:03:19 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-30 22:01:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-30 22:09:36 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.019 |  |
| 2026-01-30 22:06:08 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-01-30 22:04:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)