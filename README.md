# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_15:13:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 15:13:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:09:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.027 |  |
| 2026-05-26 15:09:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:07:50 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:07:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 15:07:11 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:06:44 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:06:36 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.096 |  |
| 2026-05-26 15:06:34 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-26 15:06:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:06:10 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-26 15:06:09 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 15:05:51 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-05-26 15:05:44 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.103 |  |
| 2026-05-26 15:05:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:05:05 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 15:04:50 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:43 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:04:26 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:26 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:04:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-05-26 15:04:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:05 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:03:33 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:03:17 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:03:08 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 15:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:49 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:02:49 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:02:36 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:25 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.141 |  |
| 2026-05-26 15:02:20 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:02:02 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 15:01:57 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:26 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:00:44 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:00:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 14:59:53 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 15:04:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.000 |  |
| 2026-05-26 15:06:34 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-26 15:06:10 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-26 15:03:08 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 15:02:02 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 15:05:05 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 15:06:09 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 15:07:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-26 15:00:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:02:49 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:26 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:13:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:03:17 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:50 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:26 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:04:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:05:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:57 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:09:05 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:07:50 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 15:06:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:20 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:03:33 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:04:05 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:00:44 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:06:44 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:07:11 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:02:36 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:04:26 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:04:43 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-26 15:05:51 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-05-26 15:09:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.027 |  |
| 2026-05-26 15:06:36 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.096 |  |
| 2026-05-26 15:05:44 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.103 |  |
| 2026-05-26 15:02:25 | Peradeniya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)