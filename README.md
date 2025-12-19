# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_02:27:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,672 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 02:27:53 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.014 |  |
| 2025-12-20 02:10:45 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.005 |  |
| 2025-12-20 02:09:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:08:58 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:08:13 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:07:49 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:06:58 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:06:42 | Padiyathalawa (Maduru Oya) | 1.57 | 🟢 Normal | -0.056 |  |
| 2025-12-20 02:06:33 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 02:06:28 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:05:43 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-20 02:04:57 | Manampitiya (Mahaweli Ganga) | 4.25 | 🟡 Alert | 0.000 |  |
| 2025-12-20 02:04:29 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 02:03:49 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:03:48 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:27 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:22 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:03:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-20 02:03:05 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-20 02:02:47 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.030 |  |
| 2025-12-20 02:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-20 02:02:41 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:02:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:02:02 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:59 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:42 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:32 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:01:28 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 02:00:41 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2025-12-20 02:00:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-20 01:47:38 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 01:45:55 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 01:40:48 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 02:04:29 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 02:04:57 | Manampitiya (Mahaweli Ganga) | 4.25 | 🟡 Alert | 0.000 |  |
| 2025-12-20 02:00:28 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-20 02:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 01:09:42 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 02:01:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 02:03:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-20 02:06:33 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 01:00:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:28 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:03:22 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:08:58 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:59 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:07:49 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:02:02 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:09:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:06:28 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 01:40:48 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:08:13 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:03:49 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 01:47:38 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:28 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:02:41 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:01:32 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 02:10:45 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.005 |  |
| 2025-12-20 02:06:58 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:27 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:03:48 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-20 02:27:53 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.014 |  |
| 2025-12-20 02:05:43 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-20 02:03:05 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-20 02:02:47 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.030 |  |
| 2025-12-20 02:00:41 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2025-12-20 02:06:42 | Padiyathalawa (Maduru Oya) | 1.57 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)