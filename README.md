# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_10:25:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 10:25:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:19:47 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:14:33 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-17 10:13:23 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-17 10:09:42 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:12 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:08:57 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-01-17 10:08:14 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:07:46 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-01-17 10:07:17 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-01-17 10:06:28 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:05:46 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-01-17 10:05:30 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-17 10:05:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:05:03 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-01-17 10:04:24 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:04:19 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-17 10:03:36 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.070 |  |
| 2026-01-17 10:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:17 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:02:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:30 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-01-17 10:02:24 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:11 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-01-17 10:02:08 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:50 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:01:30 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:28 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:27 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:17 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:01:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:00:59 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:00:30 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 10:05:03 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-01-17 10:05:46 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-01-17 10:05:30 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-17 10:13:23 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-17 10:04:19 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-17 10:01:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:00:59 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:01:17 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 10:14:33 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-17 10:01:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:30 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:02:08 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:50 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:42 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:04:24 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:27 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:08:14 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:12 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:05:23 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:28 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:17 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:09:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:01:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:19:47 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:25:04 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:03:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 10:02:30 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:24 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:06:28 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:00:30 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-17 10:02:11 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-01-17 10:07:46 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.011 |  |
| 2026-01-17 10:08:57 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-01-17 10:07:17 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-01-17 10:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-01-17 10:03:36 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)