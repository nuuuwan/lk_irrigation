# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_03:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,160 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 03:16:54 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-07-09 03:15:31 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-09 03:09:31 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-09 03:07:46 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:06:23 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-09 03:06:09 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:47 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:45 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:37 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.181 |  |
| 2026-07-09 03:05:31 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:09 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 03:05:03 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 03:04:57 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:04:14 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:04:10 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:59 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:30 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:24 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:04 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:02:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-07-09 03:02:16 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:02:05 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-09 03:02:00 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-09 03:01:32 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:01:20 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:58 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:53 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-07-09 03:00:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:14 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-07-09 02:46:26 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 03:02:50 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-07-09 03:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-09 03:09:31 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-09 03:05:03 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 03:05:09 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 03:03:04 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:01:32 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:02:16 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:04:10 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:30 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:08:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:06:09 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:24 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:59 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:31 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:07:46 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:45 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:32 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:03:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:58 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:04:14 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:05:47 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:15:31 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:08:19 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:02:00 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:04:57 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 03:00:53 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-07-09 02:46:26 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-07-09 03:16:54 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-07-09 03:06:23 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-07-09 03:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-09 03:02:05 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-09 00:02:45 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-07-09 03:05:37 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)