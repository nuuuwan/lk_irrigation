# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_05:42:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,523 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 05:42:24 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:36:06 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-29 05:36:05 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-05-29 05:17:19 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:09:36 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.301 |  |
| 2026-05-29 05:09:01 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-29 05:08:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.108 |  |
| 2026-05-29 05:07:20 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-29 05:06:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-05-29 05:06:28 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-05-29 05:06:28 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.135 |  |
| 2026-05-29 05:06:23 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.153 |  |
| 2026-05-29 05:05:55 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:05:53 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:05:52 | Magura (Kalu Ganga) | 4.62 | 🟡 Alert | -0.096 |  |
| 2026-05-29 05:05:43 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-05-29 05:05:19 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-29 05:04:51 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.154 |  |
| 2026-05-29 05:04:40 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.111 |  |
| 2026-05-29 05:03:51 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:03:51 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:03:39 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 7.579 | 🔺 Rising |
| 2026-05-29 05:03:20 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 7.579 | 🔺 Rising |
| 2026-05-29 05:03:18 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-05-29 05:03:16 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 03:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-05-29 05:36:05 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-05-29 05:05:52 | Magura (Kalu Ganga) | 4.62 | 🟡 Alert | -0.096 |  |
| 2026-05-29 05:03:39 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 7.579 | 🔺 Rising |
| 2026-05-29 05:03:18 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-05-29 05:09:01 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-29 05:05:43 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-05-29 05:36:06 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-29 05:05:19 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-29 05:07:20 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-29 05:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 05:02:06 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 05:02:53 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 05:03:51 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:42:24 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:00:59 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:03:51 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:04:40 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:02:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:02:40 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:17:19 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:05:55 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-29 05:06:28 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-05-29 05:01:09 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 05:01:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-05-29 05:01:57 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2026-05-29 05:01:52 | Glencourse (Kelani Ganga) | 12.07 | 🟢 Normal | -0.059 |  |
| 2026-05-29 05:06:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-05-29 05:03:16 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.078 |  |
| 2026-05-29 05:08:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.108 |  |
| 2026-05-29 05:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.111 |  |
| 2026-05-29 05:06:28 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.135 |  |
| 2026-05-29 04:07:07 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.146 |  |
| 2026-05-29 05:06:23 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.153 |  |
| 2026-05-29 05:04:51 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.154 |  |
| 2026-05-29 05:09:36 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.301 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)