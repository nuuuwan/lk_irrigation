# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_13:17:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 13:17:49 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:13:50 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-23 13:11:55 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.035 |  |
| 2026-05-23 13:11:21 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-05-23 13:10:34 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:07:32 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:07:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:07:03 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:06:42 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.074 |  |
| 2026-05-23 13:06:39 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:06:05 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-05-23 13:06:05 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | 0.000 |  |
| 2026-05-23 13:05:35 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:05:14 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-05-23 13:05:02 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.031 |  |
| 2026-05-23 13:04:44 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:04:38 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-05-23 13:04:33 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-05-23 13:04:22 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:03:42 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:03:41 | Rathnapura (Kalu Ganga) | 5.92 | 🟡 Alert | -0.060 |  |
| 2026-05-23 13:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:03:35 | Ellagawa (Kalu Ganga) | 10.23 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-23 13:03:21 | Hanwella (Kelani Ganga) | 6.58 | 🟢 Normal | -0.090 |  |
| 2026-05-23 13:03:18 | Dunamale (Aththanagalu Oya) | 5.06 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 13:02:59 | Putupaula (Kalu Ganga) | 3.09 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-23 13:02:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-23 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 13:02:39 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:02:15 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:02:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 13:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:01:29 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:01:28 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:12 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:01:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:04 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:00:59 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-23 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:00:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 13:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 13:03:18 | Dunamale (Aththanagalu Oya) | 5.06 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 13:02:59 | Putupaula (Kalu Ganga) | 3.09 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-23 13:03:35 | Ellagawa (Kalu Ganga) | 10.23 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-05-23 13:06:05 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | 0.000 |  |
| 2026-05-23 13:03:41 | Rathnapura (Kalu Ganga) | 5.92 | 🟡 Alert | -0.060 |  |
| 2026-05-23 13:02:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-23 13:00:59 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-23 13:02:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 13:02:39 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:28 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:10:34 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:17:49 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:07:03 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:02:15 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:03:42 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:07:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:04:22 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:06:39 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:13:50 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-05-23 13:06:05 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-05-23 13:01:12 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:07:32 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:01:29 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:04:44 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:00:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:01:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-23 13:04:38 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-05-23 13:11:21 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-05-23 13:05:14 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-05-23 13:04:33 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-05-23 13:05:02 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.031 |  |
| 2026-05-23 13:11:55 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.035 |  |
| 2026-05-23 13:06:42 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.074 |  |
| 2026-05-23 13:03:21 | Hanwella (Kelani Ganga) | 6.58 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)