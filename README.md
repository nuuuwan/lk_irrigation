# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_22:28:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 22:28:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-28 22:20:17 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:19:04 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-28 22:14:26 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-01-28 22:12:49 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:09:38 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:08:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:06:51 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-01-28 22:06:39 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:06:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:05:49 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-28 22:05:40 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:05:37 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-28 22:04:52 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-28 22:04:28 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.020 |  |
| 2026-01-28 22:04:26 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:04:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-28 22:03:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:33 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:24 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.235 |  |
| 2026-01-28 22:02:43 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:34 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:32 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:25 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:59 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:53 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:51 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:46 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:32 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-01-28 22:01:30 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:09 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-28 22:00:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 22:14:26 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-01-28 22:05:49 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-28 22:19:04 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-28 22:28:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-28 22:04:52 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-28 18:04:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 22:01:30 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:51 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:20:17 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:59 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:05:40 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-28 21:06:37 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:43 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:46 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:25 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:01:53 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:33 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:03:24 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:34 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:12:49 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:04:26 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:06:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:08:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:09:38 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:06:39 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:00:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:02:32 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-28 22:04:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-28 18:00:30 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-28 22:01:09 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-28 22:01:32 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-01-28 22:05:37 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-28 22:04:28 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.020 |  |
| 2026-01-28 22:06:51 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-01-28 18:05:41 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.084 |  |
| 2026-01-28 22:03:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.235 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)