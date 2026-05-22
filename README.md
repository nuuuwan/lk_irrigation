# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_00:13:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,180 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 00:13:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.052 |  |
| 2026-05-23 00:12:36 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-23 00:10:37 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | -0.015 |  |
| 2026-05-23 00:09:09 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 00:08:50 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.009 |  |
| 2026-05-23 00:08:48 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.015 |  |
| 2026-05-23 00:08:40 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-05-23 00:07:58 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.015 |  |
| 2026-05-23 00:07:37 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:06:20 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.039 |  |
| 2026-05-23 00:05:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:05:46 | Rathnapura (Kalu Ganga) | 6.91 | 🟡 Alert | -0.097 |  |
| 2026-05-23 00:05:34 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 00:05:13 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 1.796 | 🔺 Rising |
| 2026-05-23 00:04:46 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:04:13 | Ellagawa (Kalu Ganga) | 9.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 00:04:08 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:04:01 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-05-23 00:03:25 | Glencourse (Kelani Ganga) | 14.16 | 🟢 Normal | -0.041 |  |
| 2026-05-23 00:03:24 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-23 00:03:08 | Hanwella (Kelani Ganga) | 7.86 | 🟡 Alert | -0.063 |  |
| 2026-05-23 00:02:59 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:02:52 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.032 |  |
| 2026-05-23 00:02:40 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:02:36 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 00:02:34 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 00:02:23 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:59 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.044 |  |
| 2026-05-23 00:01:39 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:18 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:15 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:00:45 | Magura (Kalu Ganga) | 4.23 | 🟡 Alert | -0.022 |  |
| 2026-05-23 00:00:33 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:00:28 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 00:05:34 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 00:10:37 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | -0.015 |  |
| 2026-05-23 00:00:45 | Magura (Kalu Ganga) | 4.23 | 🟡 Alert | -0.022 |  |
| 2026-05-23 00:13:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.052 |  |
| 2026-05-23 00:03:08 | Hanwella (Kelani Ganga) | 7.86 | 🟡 Alert | -0.063 |  |
| 2026-05-23 00:05:46 | Rathnapura (Kalu Ganga) | 6.91 | 🟡 Alert | -0.097 |  |
| 2026-05-23 00:05:13 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 1.796 | 🔺 Rising |
| 2026-05-22 22:00:54 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 1.017 | 🔺 Rising |
| 2026-05-23 00:12:36 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-23 00:04:13 | Ellagawa (Kalu Ganga) | 9.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 23:01:17 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 00:01:39 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:02:40 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:00:33 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:04:46 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:07:37 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:15 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:02:23 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:18 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:02:59 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:05:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:00:28 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:04:08 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:08:50 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.009 |  |
| 2026-05-23 00:09:09 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 00:03:24 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 00:08:40 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-05-23 00:08:48 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.015 |  |
| 2026-05-23 00:07:58 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.015 |  |
| 2026-05-22 23:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-23 00:02:52 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.032 |  |
| 2026-05-23 00:06:20 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.039 |  |
| 2026-05-23 00:04:01 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-05-23 00:03:25 | Glencourse (Kelani Ganga) | 14.16 | 🟢 Normal | -0.041 |  |
| 2026-05-23 00:01:59 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)