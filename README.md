# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_22:14:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 22:14:49 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:11:34 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:10:58 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:10:47 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 22:10:13 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-31 22:09:40 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:09:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:09:06 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-31 22:07:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 22:07:17 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-31 22:06:38 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:05:48 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:05:21 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.111 |  |
| 2026-07-31 22:05:14 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:05:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:55 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:04:38 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:04:22 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:03 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:03:41 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.098 |  |
| 2026-07-31 22:03:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:03:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 22:03:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:02:50 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 22:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:01:54 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:19 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:16 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:14 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:08 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-31 22:00:50 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 22:01:08 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-31 22:09:06 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-31 22:10:13 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-31 22:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 22:07:17 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-31 22:02:50 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 22:07:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 22:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:03:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:03:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:09:40 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 22:10:47 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:14 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:03:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:22 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:19 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:05:48 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:14:49 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:38 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:11:34 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 21:02:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:10:58 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:16 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:04:03 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:05:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:00:50 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:09:34 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:01:54 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 22:05:14 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:04:55 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:04:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:06:38 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-07-31 22:03:41 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.098 |  |
| 2026-07-31 22:05:21 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)