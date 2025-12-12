# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_19:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 19:10:21 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.000 |  |
| 2025-12-12 19:09:59 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-12 19:09:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:07:19 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2025-12-12 19:06:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 19:06:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:05:56 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 19:05:48 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.091 |  |
| 2025-12-12 19:05:20 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:05:14 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-12 19:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.013 |  |
| 2025-12-12 19:04:55 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 19:04:39 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-12 19:04:36 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:04:08 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-12 19:03:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2025-12-12 19:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.030 |  |
| 2025-12-12 19:03:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:03:28 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-12 19:02:55 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:02:47 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 19:02:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2025-12-12 19:02:19 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 19:02:18 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-12 19:02:08 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.089 |  |
| 2025-12-12 19:01:58 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:42 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:41 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:35 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:23 | Manampitiya (Mahaweli Ganga) | 3.00 | 🟡 Alert | -0.061 |  |
| 2025-12-12 19:00:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:00:14 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:18:41 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 19:10:21 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.000 |  |
| 2025-12-12 19:01:23 | Manampitiya (Mahaweli Ganga) | 3.00 | 🟡 Alert | -0.061 |  |
| 2025-12-12 19:03:28 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-12 19:02:47 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 19:05:56 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 19:02:19 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 19:05:14 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-12 19:09:59 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-12 19:06:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 19:04:55 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 19:01:41 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:58 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:42 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:04:36 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:00:14 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:03:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:00:56 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:09:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:02:55 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:05:20 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:01:35 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:06:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:07:19 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2025-12-12 18:05:16 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.009 |  |
| 2025-12-12 17:05:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-12 19:04:08 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-12 18:04:49 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-12 19:02:18 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-12 19:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.013 |  |
| 2025-12-12 19:04:39 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-12 18:05:21 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.020 |  |
| 2025-12-12 19:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.030 |  |
| 2025-12-12 19:02:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2025-12-12 19:02:08 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.089 |  |
| 2025-12-12 19:05:48 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.091 |  |
| 2025-12-12 19:03:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)