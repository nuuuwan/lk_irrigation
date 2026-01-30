# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_19:07:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 19:07:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:06:43 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-30 19:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:05:56 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-30 19:05:25 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:04:51 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-01-30 19:04:40 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:04:37 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-30 19:04:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:04:21 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-30 19:03:44 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 19:03:40 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 19:03:07 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:49 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:45 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:38 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-30 19:02:15 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:04 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:01:37 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-30 19:01:33 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:01:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-30 19:01:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-30 19:01:14 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 19:00:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:00:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-30 18:11:27 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 19:01:37 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-30 18:01:57 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-30 19:06:43 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-30 19:01:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-30 19:00:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-30 19:01:14 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 19:02:38 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-30 19:03:40 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 19:03:44 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 19:00:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:04 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:40 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:03:07 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:15 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:45 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:15 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:05:25 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:02:49 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:04:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:05:03 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:06:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:01:33 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:04:40 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:07:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:05:14 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:04:40 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 19:05:56 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-30 19:04:21 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-30 19:04:37 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-30 19:01:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-30 18:02:17 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-01-30 18:04:17 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.019 |  |
| 2026-01-30 19:04:51 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-01-30 18:01:52 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)