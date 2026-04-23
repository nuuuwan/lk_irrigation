# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_20:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 20:10:56 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.009 |  |
| 2026-04-23 20:10:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.679 | 🔺 Rising |
| 2026-04-23 20:10:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 20:09:46 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.010 |  |
| 2026-04-23 20:07:24 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 20:07:10 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-23 20:06:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-23 20:06:56 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:06:49 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.112 |  |
| 2026-04-23 20:06:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-23 20:06:28 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-04-23 20:05:32 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:05:19 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 20:04:43 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-23 20:04:26 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 20:04:23 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-04-23 20:04:11 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-23 20:03:16 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-23 20:02:57 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-04-23 20:02:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-23 20:02:28 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 20:02:27 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-04-23 20:02:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:02:05 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:01:57 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:01:54 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-04-23 20:01:44 | Thanamalwila (Kirindi Oya) | 2.29 | 🟢 Normal | -0.075 |  |
| 2026-04-23 20:01:40 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:01:10 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.081 |  |
| 2026-04-23 20:00:29 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.289 |  |
| 2026-04-23 19:35:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | 0.679 | 🔺 Rising |
| 2026-04-23 19:27:45 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.084 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 20:10:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.679 | 🔺 Rising |
| 2026-04-23 20:02:27 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-04-23 19:02:11 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-23 20:07:10 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-23 20:03:22 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-23 20:03:16 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-23 19:05:05 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 20:04:43 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-23 20:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-23 20:02:28 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 20:04:26 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-23 19:04:38 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 20:05:19 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 20:07:24 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 20:10:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:02:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:01:57 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:04:11 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:02:05 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:01:54 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:06:56 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-23 20:10:56 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.009 |  |
| 2026-04-23 20:06:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 20:09:46 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.010 |  |
| 2026-04-23 20:04:23 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-04-23 20:05:32 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:01:40 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:02:52 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-04-23 20:06:28 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-04-23 20:02:57 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-04-23 20:06:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-23 20:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-04-23 20:01:44 | Thanamalwila (Kirindi Oya) | 2.29 | 🟢 Normal | -0.075 |  |
| 2026-04-23 20:01:10 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.081 |  |
| 2026-04-23 20:06:49 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.112 |  |
| 2026-04-23 20:00:29 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)