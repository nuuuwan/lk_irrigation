# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_12:09:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 12:09:36 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.426 | 🔺 Rising |
| 2026-05-13 12:09:25 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:08:26 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 12:06:06 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-13 12:06:05 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-13 12:05:45 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2026-05-13 12:05:44 | Rathnapura (Kalu Ganga) | 6.14 | 🟡 Alert | 0.273 | 🔺 Rising |
| 2026-05-13 12:05:34 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 12:05:10 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-13 12:04:45 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 12:04:43 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:04:31 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-13 12:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-05-13 12:04:18 | Galgamuwa (Mee Oya) | 2.56 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-05-13 12:04:18 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:04:00 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-05-13 12:03:50 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-05-13 12:03:42 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-13 12:03:28 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:03:26 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | -1.159 |  |
| 2026-05-13 12:03:09 | Pitabeddara (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-13 12:03:04 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-13 12:03:03 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:02:57 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:02:55 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:02:44 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-13 12:02:38 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:02:38 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-05-13 12:01:58 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-13 12:01:55 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:01:54 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 12:01:32 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:01:25 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-05-13 12:01:11 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-05-13 12:01:11 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-13 12:01:01 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-13 12:00:08 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.011 |  |
| 2026-05-13 11:59:55 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 12:09:36 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.426 | 🔺 Rising |
| 2026-05-13 12:05:44 | Rathnapura (Kalu Ganga) | 6.14 | 🟡 Alert | 0.273 | 🔺 Rising |
| 2026-05-13 12:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-05-13 12:05:45 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.744 | 🔺 Rising |
| 2026-05-13 12:04:18 | Galgamuwa (Mee Oya) | 2.56 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-05-13 12:02:38 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-05-13 12:06:06 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-13 12:04:45 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-13 12:08:26 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 12:05:34 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-13 12:01:54 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 12:01:11 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-13 12:03:09 | Pitabeddara (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-13 12:05:10 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-13 12:01:01 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-13 12:01:58 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-13 12:03:42 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-13 12:02:44 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-13 12:06:05 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-13 12:02:57 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:03:28 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:09:25 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 12:01:25 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 12:03:03 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:01:32 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:02:55 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:04:18 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:02:38 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:01:55 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:04:43 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 12:04:31 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-13 12:03:04 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-13 12:00:08 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.011 |  |
| 2026-05-13 12:04:00 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-05-13 12:01:11 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.032 |  |
| 2026-05-13 11:59:55 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.042 |  |
| 2026-05-13 12:03:50 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-05-13 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-05-13 12:03:26 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | -1.159 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)