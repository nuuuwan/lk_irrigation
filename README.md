# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_04:05:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 04:05:17 | Manampitiya (Mahaweli Ganga) | 3.15 | 🟡 Alert | -0.099 |  |
| 2025-12-21 04:04:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:04:20 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2025-12-21 04:04:16 | Horowpothana (Yan Oya) | 5.95 | 🟢 Normal | -0.066 |  |
| 2025-12-21 04:03:48 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-21 04:03:41 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-21 04:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-21 04:03:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2025-12-21 04:03:00 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:02:48 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:02:47 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-21 04:02:11 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:43 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-21 04:01:35 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:19 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.048 |  |
| 2025-12-21 04:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:00:46 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:46:09 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:35:27 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -18.000 |  |
| 2025-12-21 03:35:25 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -18.000 |  |
| 2025-12-21 03:35:24 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -18.000 |  |
| 2025-12-21 03:13:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:13:44 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:11:36 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.048 |  |
| 2025-12-21 03:11:17 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-21 03:08:29 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-21 03:08:09 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 03:07:12 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-21 04:05:17 | Manampitiya (Mahaweli Ganga) | 3.15 | 🟡 Alert | -0.099 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-21 04:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-21 03:03:40 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-21 04:03:48 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-21 03:08:29 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-21 04:02:47 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-21 03:08:09 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 03:11:17 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 03:02:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:00:46 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:04 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:35 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:02:11 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:04 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:04:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:01:19 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:04:02 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:02:48 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:03:00 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:13:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:03:57 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:06:14 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 04:04:20 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2025-12-21 04:03:41 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:04:03 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2025-12-21 04:01:43 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-21 02:09:20 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2025-12-21 04:01:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.048 |  |
| 2025-12-21 03:01:37 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2025-12-21 04:04:16 | Horowpothana (Yan Oya) | 5.95 | 🟢 Normal | -0.066 |  |
| 2025-12-21 04:03:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2025-12-21 03:07:12 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.103 |  |
| 2025-12-21 03:04:00 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.113 |  |
| 2025-12-21 03:35:27 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)