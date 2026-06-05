# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_20:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,408 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 20:15:27 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.033 |  |
| 2026-06-05 20:11:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 20:09:31 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:09:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:09:06 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-05 20:08:59 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 20:08:10 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-06-05 20:08:07 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 20:07:44 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-05 20:06:38 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 20:06:35 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:05:52 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-05 20:05:45 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.051 |  |
| 2026-06-05 20:05:34 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 20:05:29 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-06-05 20:05:27 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:05:16 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:05:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-06-05 20:04:44 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:04:18 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-06-05 20:04:09 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:03:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:03:30 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:03:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:03:07 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 20:02:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-05 20:02:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-05 20:02:20 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-05 20:02:05 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-06-05 20:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:01:29 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 20:08:10 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-06-05 20:02:20 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-05 20:02:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-05 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 20:08:59 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 20:09:06 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-05 20:05:34 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 20:07:44 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-05 20:06:38 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 20:03:07 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 20:08:07 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 20:11:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 20:03:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:46 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:03:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:05:16 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:05:27 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:09:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:04:44 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:00:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:01:29 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:03:30 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-05 20:06:35 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:09:31 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:01:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:04:09 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.010 |  |
| 2026-06-05 20:05:52 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-05 20:04:18 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-06-05 20:05:29 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-05 20:02:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-05 20:02:05 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-06-05 20:15:27 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.033 |  |
| 2026-06-05 20:05:45 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.051 |  |
| 2026-06-05 20:05:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)