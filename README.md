# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_19:36:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,757 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 19:36:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:17:32 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.016 |  |
| 2026-01-03 19:16:50 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-01-03 19:15:50 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-01-03 19:13:50 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-03 19:11:55 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-01-03 19:10:10 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:09:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-01-03 19:09:36 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:05:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:05:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:05:25 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:04:56 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-03 19:04:39 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-01-03 19:04:39 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:04:28 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.075 |  |
| 2026-01-03 19:04:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-03 19:04:05 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:03:57 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:03:51 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:03:42 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:03:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:03:24 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:02:54 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:02:40 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:02:20 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-01-03 19:02:11 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 19:02:01 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 19:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:01:18 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:01:13 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:01:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.022 |  |
| 2026-01-03 19:01:06 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-01-03 19:00:13 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:56:08 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 19:04:39 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-01-03 19:04:19 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-03 19:04:56 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-03 19:13:50 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-03 19:02:11 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 19:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 19:00:13 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:04:39 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:01:13 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:05:25 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:09:36 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:02:54 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:02:01 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:03:57 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:03:51 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:36:17 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:05:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:10:10 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 19:11:55 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-01-03 19:04:05 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:01:18 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:03:42 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:05:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-03 19:02:20 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-01-03 19:01:06 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-01-03 19:17:32 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.016 |  |
| 2026-01-03 19:15:50 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-01-03 19:03:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:02:40 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:03:24 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-03 19:01:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.022 |  |
| 2026-01-03 19:09:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-01-03 19:16:50 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 19:04:28 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)