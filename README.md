# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_17:20:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 17:20:50 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-05-15 17:19:44 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:12:54 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:12:33 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-15 17:11:45 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-05-15 17:10:45 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:10:29 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2026-05-15 17:09:19 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:09:17 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.049 |  |
| 2026-05-15 17:08:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 17:08:32 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.028 |  |
| 2026-05-15 17:08:27 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.009 |  |
| 2026-05-15 17:07:35 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.075 |  |
| 2026-05-15 17:07:26 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-15 17:07:12 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 17:06:43 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-15 17:06:36 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.090 |  |
| 2026-05-15 17:06:27 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:06:03 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.071 |  |
| 2026-05-15 17:05:35 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-15 17:05:34 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.092 |  |
| 2026-05-15 17:04:51 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:04:47 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 17:04:13 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:04:10 | Hanwella (Kelani Ganga) | 5.23 | 🟢 Normal | -0.128 |  |
| 2026-05-15 17:03:51 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-15 17:03:30 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:21 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:18 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | -0.030 |  |
| 2026-05-15 17:02:59 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:02:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:02:29 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-15 17:01:52 | Galgamuwa (Mee Oya) | 4.00 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-05-15 17:01:51 | Galgamuwa (Mee Oya) | 3.95 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-05-15 17:01:49 | Giriulla (Maha Oya) | 2.96 | 🟢 Normal | -0.071 |  |
| 2026-05-15 17:01:28 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 17:00:14 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 16:11:58 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 17:08:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 17:06:36 | Magura (Kalu Ganga) | 4.34 | 🟡 Alert | -0.090 |  |
| 2026-05-15 17:01:52 | Galgamuwa (Mee Oya) | 4.00 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-05-15 17:07:26 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-15 17:03:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-15 17:06:43 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-15 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 17:07:12 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 17:01:28 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 17:04:47 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 17:02:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:51 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:12:54 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:30 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:09:19 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:03:21 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:02:59 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:06:27 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:04:51 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:04:13 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:10:45 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:19:44 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 17:20:50 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-05-15 17:08:27 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.009 |  |
| 2026-05-15 17:11:45 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-05-15 17:10:29 | Baddegama (Gin Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2026-05-15 17:05:35 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-15 17:02:29 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-15 17:00:14 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-05-15 17:08:32 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.028 |  |
| 2026-05-15 17:03:18 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | -0.030 |  |
| 2026-05-15 17:12:33 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-15 17:09:17 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.049 |  |
| 2026-05-15 17:06:03 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.071 |  |
| 2026-05-15 17:01:49 | Giriulla (Maha Oya) | 2.96 | 🟢 Normal | -0.071 |  |
| 2026-05-15 17:07:35 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.075 |  |
| 2026-05-15 17:05:34 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | -0.092 |  |
| 2026-05-15 17:04:10 | Hanwella (Kelani Ganga) | 5.23 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)