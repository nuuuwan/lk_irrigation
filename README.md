# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_19:46:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,025 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 19:46:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.063 |  |
| 2026-05-03 19:22:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:18:20 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:15:00 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.024 |  |
| 2026-05-03 19:14:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:11:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-05-03 19:09:28 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:08:40 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:08:27 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:07:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.018 |  |
| 2026-05-03 19:07:15 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-05-03 19:06:39 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-05-03 19:05:39 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:05:23 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-05-03 19:05:15 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-03 19:05:09 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:03:50 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:03:49 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:03:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 19:03:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:03:12 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:02:56 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:56 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2026-05-03 19:02:49 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-03 19:02:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.162 |  |
| 2026-05-03 19:02:18 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:01:33 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.012 |  |
| 2026-05-03 19:01:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-05-03 19:01:11 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-03 19:01:03 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-05-03 19:00:56 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:00:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.093 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 19:01:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-05-03 19:05:15 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-03 19:02:49 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-03 19:01:11 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 19:03:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 19:03:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:05:39 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:56 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:09:28 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:18:20 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:03:50 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:18 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:08:27 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:08:40 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:14:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:03:49 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:22:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:02:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:05:09 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:00:56 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:03:12 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.010 |  |
| 2026-05-03 19:01:03 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-05-03 19:01:33 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.012 |  |
| 2026-05-03 19:11:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-05-03 19:07:20 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.018 |  |
| 2026-05-03 19:15:00 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.024 |  |
| 2026-05-03 19:02:56 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2026-05-03 19:06:39 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-05-03 19:05:23 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-05-03 19:07:15 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-05-03 19:46:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.063 |  |
| 2026-05-03 19:00:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.093 |  |
| 2026-05-03 19:02:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)