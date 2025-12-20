# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_12:11:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 12:11:34 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:09:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2025-12-20 12:09:13 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | -0.029 |  |
| 2025-12-20 12:07:40 | Thanthirimale (Malwathu Oya) | 5.48 | 🟡 Alert | -0.019 |  |
| 2025-12-20 12:07:32 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2025-12-20 12:07:21 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:06:44 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:06:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-20 12:04:56 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:35 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-20 12:04:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2025-12-20 12:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:19 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.030 |  |
| 2025-12-20 12:04:13 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:00 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:47 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:21 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:15 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.068 |  |
| 2025-12-20 12:03:09 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:05 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:02:59 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:55 | Weraganthota (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.021 |  |
| 2025-12-20 12:02:51 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:40 | Manampitiya (Mahaweli Ganga) | 3.80 | 🟡 Alert | -0.119 |  |
| 2025-12-20 12:02:16 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 12:02:07 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:01:58 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:01:46 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:01:45 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 12:01:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-20 12:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:01:28 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:01:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:59:04 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | -0.021 |  |
| 2025-12-20 11:43:25 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2025-12-20 11:26:03 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:13:43 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 12:07:40 | Thanthirimale (Malwathu Oya) | 5.48 | 🟡 Alert | -0.019 |  |
| 2025-12-20 11:59:04 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | -0.021 |  |
| 2025-12-20 12:02:40 | Manampitiya (Mahaweli Ganga) | 3.80 | 🟡 Alert | -0.119 |  |
| 2025-12-20 12:06:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-20 12:04:35 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-20 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 12:01:45 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 12:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:00 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:21 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:06:44 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:56 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:01:46 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:13 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:11:34 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:07:21 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:02:16 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:03:05 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:02:51 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:47 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:59 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:09 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:01:28 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:07 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:01:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:01:58 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:03:24 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:07:32 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2025-12-20 12:01:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-20 12:02:55 | Weraganthota (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.021 |  |
| 2025-12-20 12:09:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2025-12-20 12:04:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2025-12-20 12:09:13 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | -0.029 |  |
| 2025-12-20 12:04:19 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.030 |  |
| 2025-12-20 12:03:15 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)