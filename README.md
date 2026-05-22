# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_02:51:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,240 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 02:51:19 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 02:23:42 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-23 02:20:41 | Glencourse (Kelani Ganga) | 13.22 | 🟢 Normal | -0.605 |  |
| 2026-05-23 02:09:10 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-05-23 02:07:21 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:06:21 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.056 |  |
| 2026-05-23 02:06:11 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-05-23 02:05:49 | Hanwella (Kelani Ganga) | 7.68 | 🟡 Alert | -0.090 |  |
| 2026-05-23 02:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.028 |  |
| 2026-05-23 02:04:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 02:04:31 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-23 02:04:14 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-05-23 02:03:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:02:47 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-23 02:02:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:02:22 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:02:20 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.083 |  |
| 2026-05-23 02:02:11 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-05-23 02:02:11 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 02:01:45 | Ellagawa (Kalu Ganga) | 9.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 02:01:43 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-23 02:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:01:30 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-23 02:01:27 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 02:51:19 | Dunamale (Aththanagalu Oya) | 5.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 01:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-05-23 02:06:11 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-05-23 00:00:45 | Magura (Kalu Ganga) | 4.23 | 🟡 Alert | -0.022 |  |
| 2026-05-23 02:02:20 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.083 |  |
| 2026-05-23 02:05:49 | Hanwella (Kelani Ganga) | 7.68 | 🟡 Alert | -0.090 |  |
| 2026-05-23 02:02:47 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-23 02:01:12 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-23 01:53:53 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-23 02:04:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 02:01:45 | Ellagawa (Kalu Ganga) | 9.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 02:23:42 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-23 02:02:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:03:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:01:27 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:02:22 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:58:51 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:01:15 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 00:05:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 02:07:21 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:33:56 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.007 |  |
| 2026-05-23 01:05:30 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-23 02:01:30 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 02:01:43 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-23 00:07:58 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.015 |  |
| 2026-05-23 02:04:31 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-23 02:09:10 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-05-23 02:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.028 |  |
| 2026-05-23 01:08:59 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | -0.028 |  |
| 2026-05-23 02:04:14 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-23 02:02:11 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-05-23 01:12:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.033 |  |
| 2026-05-23 02:06:21 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.056 |  |
| 2026-05-23 02:20:41 | Glencourse (Kelani Ganga) | 13.22 | 🟢 Normal | -0.605 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)