# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_19:38:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 19:38:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-05-09 19:16:12 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 19:15:58 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:15:02 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:13:25 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.017 |  |
| 2026-05-09 19:11:39 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-09 19:10:51 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 19:10:35 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-05-09 19:10:24 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.060 |  |
| 2026-05-09 19:09:41 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 19:09:40 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.035 |  |
| 2026-05-09 19:09:09 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2026-05-09 19:08:35 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 19:07:27 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-05-09 19:06:39 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-09 19:06:01 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:05:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:04:58 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:04:38 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:04:33 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.113 |  |
| 2026-05-09 19:04:20 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:04:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:03:53 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-05-09 19:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:03:26 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.124 |  |
| 2026-05-09 19:02:37 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-09 19:02:30 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-09 19:02:28 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:01:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:01:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 19:01:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:01:44 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.035 |  |
| 2026-05-09 19:01:41 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.041 |  |
| 2026-05-09 19:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 19:01:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 19:01:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-05-09 19:00:37 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:00:36 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 19:02:37 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 19:02:30 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-09 19:01:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 19:10:51 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 19:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 19:09:41 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 19:08:35 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 19:16:12 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 19:01:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:04:58 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:00:37 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:01:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:04:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:15:58 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:15:02 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:05:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 19:11:39 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-09 19:00:36 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-09 19:01:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 19:01:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-05-09 19:13:25 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.017 |  |
| 2026-05-09 19:07:27 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-05-09 19:06:39 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-09 19:10:35 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-05-09 19:03:53 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-05-09 19:01:44 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.035 |  |
| 2026-05-09 19:09:40 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.035 |  |
| 2026-05-09 19:02:28 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:04:38 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-09 19:01:41 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.041 |  |
| 2026-05-09 19:38:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 19:10:24 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.060 |  |
| 2026-05-09 19:09:09 | Katharagama (Menik Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 19:04:33 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.113 |  |
| 2026-05-09 19:03:26 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)