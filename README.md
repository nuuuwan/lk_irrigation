# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_05:18:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,388 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 05:18:42 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.014 |  |
| 2026-05-13 05:13:38 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:12:54 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.185 |  |
| 2026-05-13 05:11:40 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.055 |  |
| 2026-05-13 05:09:53 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-05-13 05:09:19 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-13 05:09:05 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.038 |  |
| 2026-05-13 05:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-13 05:07:57 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.034 |  |
| 2026-05-13 05:07:33 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | -0.199 |  |
| 2026-05-13 05:07:29 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-13 05:07:23 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.090 |  |
| 2026-05-13 05:06:39 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.100 |  |
| 2026-05-13 05:05:37 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:05:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:05:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-13 05:05:02 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-05-13 05:03:43 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.041 |  |
| 2026-05-13 05:03:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 05:03:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:14 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-05-13 05:03:00 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:36 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:07 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:01:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-13 05:01:44 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 05:01:25 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.225 |  |
| 2026-05-13 05:01:15 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:00:19 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.110 |  |
| 2026-05-13 05:00:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:48:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 05:05:02 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-05-13 05:01:44 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 05:07:29 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-13 05:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-13 04:06:25 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 05:03:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 05:09:19 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-13 04:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:06:51 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 05:05:37 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:02:07 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:01:15 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 05:05:37 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:01:46 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:14 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:00 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:00:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:03:32 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:13:38 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:02:36 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 05:18:42 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.014 |  |
| 2026-05-13 05:05:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 05:07:57 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.034 |  |
| 2026-05-13 05:09:05 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | -0.038 |  |
| 2026-05-13 05:01:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-13 05:03:43 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.041 |  |
| 2026-05-13 05:03:11 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.050 |  |
| 2026-05-13 05:11:40 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.055 |  |
| 2026-05-13 05:09:53 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-05-13 05:07:23 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.090 |  |
| 2026-05-13 05:06:39 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.100 |  |
| 2026-05-13 05:00:19 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.110 |  |
| 2026-05-13 05:12:54 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.185 |  |
| 2026-05-13 05:07:33 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | -0.199 |  |
| 2026-05-13 05:01:25 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)