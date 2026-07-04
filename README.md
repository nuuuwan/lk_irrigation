# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_05:44:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 05:44:06 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 05:35:54 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-04 05:24:27 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.002 |  |
| 2026-07-04 05:16:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:15:46 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 05:15:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-07-04 05:15:32 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-07-04 05:13:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.077 |  |
| 2026-07-04 05:11:17 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:10:48 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 05:09:48 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-07-04 05:09:01 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 05:08:59 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.091 |  |
| 2026-07-04 05:08:30 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:06:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:06:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-04 05:05:51 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-04 05:05:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-07-04 05:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-04 05:04:46 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-07-04 05:04:40 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.113 |  |
| 2026-07-04 05:04:38 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:04:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:04:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.065 |  |
| 2026-07-04 05:04:27 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:03:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-04 05:02:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:02:51 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 05:02:50 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 05:02:50 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 05:02:38 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:02:17 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-07-04 05:02:13 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:01:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.174 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 05:15:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-07-04 05:02:17 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-07-04 05:01:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-07-04 05:04:46 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-07-04 05:06:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-04 05:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-04 05:02:50 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 05:44:06 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 05:35:54 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-04 05:09:01 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 05:10:48 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 05:15:46 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 05:02:51 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 05:02:50 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 05:24:27 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.002 |  |
| 2026-07-04 05:02:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:06:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:04:27 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:01:06 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:08:30 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:04:38 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:06:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:02:38 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:04:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:02:13 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:16:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 03:01:17 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 05:11:17 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-04 05:03:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-04 05:05:51 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-04 05:09:48 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-07-04 05:05:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-07-04 05:04:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.065 |  |
| 2026-07-04 05:13:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.077 |  |
| 2026-07-04 05:08:59 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.091 |  |
| 2026-07-04 05:04:40 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)