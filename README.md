# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_12:17:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,157 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 12:17:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:09:57 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:08:23 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:08:21 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:49 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:39 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:06:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:06:46 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:06:29 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2025-12-19 12:06:06 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2025-12-19 12:05:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:05:51 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 12:05:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:05:25 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.040 |  |
| 2025-12-19 12:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-19 12:04:50 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2025-12-19 12:04:50 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.059 |  |
| 2025-12-19 12:04:44 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |
| 2025-12-19 12:04:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -36.000 |  |
| 2025-12-19 12:04:39 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:04:22 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:04:11 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 12:03:43 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:03:35 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:02:42 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 12:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-19 12:02:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:02:21 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:02:01 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:01:57 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-19 12:01:57 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.030 |  |
| 2025-12-19 12:01:31 | Horowpothana (Yan Oya) | 6.21 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-19 12:01:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:01:19 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:01:12 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:00:54 | Manampitiya (Mahaweli Ganga) | 4.70 | 🟠 Minor Flood | -0.033 |  |
| 2025-12-19 12:00:18 | Nakkala (Kumbukkan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 12:00:54 | Manampitiya (Mahaweli Ganga) | 4.70 | 🟠 Minor Flood | -0.033 |  |
| 2025-12-19 12:01:31 | Horowpothana (Yan Oya) | 6.21 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-19 12:05:51 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 12:06:06 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2025-12-19 11:02:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-19 12:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-19 12:02:42 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 12:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-19 12:04:11 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 12:02:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:01:12 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:02:21 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:09:57 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:04:39 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:06:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:07:49 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:17:19 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:16:45 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:03:35 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:05:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:06:46 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:05:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:03:43 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:08:23 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 12:02:01 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:00:18 | Nakkala (Kumbukkan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:07:39 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:01:19 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:04:22 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 12:01:57 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-19 12:06:29 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2025-12-19 12:01:57 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.030 |  |
| 2025-12-19 12:05:25 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.040 |  |
| 2025-12-19 12:04:50 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2025-12-19 12:04:50 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.059 |  |
| 2025-12-19 11:03:34 | Weraganthota (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.863 |  |
| 2025-12-19 12:04:44 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)