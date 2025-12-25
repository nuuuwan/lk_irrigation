# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_01:24:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 01:24:04 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:13:41 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-26 01:07:36 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:07:02 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:06:52 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-26 01:06:33 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:06:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:05:23 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.048 |  |
| 2025-12-26 01:05:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:05:05 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:04:32 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.117 |  |
| 2025-12-26 01:04:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:04:26 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2025-12-26 01:03:49 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:03:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2025-12-26 01:03:37 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:02:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-26 01:02:11 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.021 |  |
| 2025-12-26 01:02:04 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:01:49 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:01:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:01:45 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:01:09 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2025-12-26 01:01:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:53 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:52 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.052 |  |
| 2025-12-26 01:00:46 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:43:29 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:35:21 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 01:13:41 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-26 01:02:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-26 01:05:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:01:49 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:53 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:24:04 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:07:02 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:03:49 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:02:04 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:04:29 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:02:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:46 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:01:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:00:27 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:07:36 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:08:17 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 01:03:37 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:12:35 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.005 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 01:06:52 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-26 01:06:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:05:05 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:01:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-26 01:01:45 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:51:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.012 |  |
| 2025-12-26 00:10:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.017 |  |
| 2025-12-26 01:03:42 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2025-12-26 01:01:09 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2025-12-26 01:02:11 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.021 |  |
| 2025-12-26 00:18:14 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.025 |  |
| 2025-12-26 00:06:16 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.028 |  |
| 2025-12-26 01:04:26 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2025-12-26 01:05:23 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.048 |  |
| 2025-12-26 01:00:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.052 |  |
| 2025-12-26 00:04:02 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.099 |  |
| 2025-12-26 01:04:32 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)