# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_19:47:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,623 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 19:47:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.006 |  |
| 2025-12-17 19:26:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2025-12-17 19:08:54 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:08:00 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:07:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2025-12-17 19:07:47 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:07:42 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 19:07:28 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-17 19:06:58 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:06:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2025-12-17 19:06:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:06:11 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 19:05:56 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:05:55 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:05:44 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 19:04:52 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:04:43 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-17 19:04:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 19:04:28 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 19:04:26 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:04:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-17 19:03:22 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 19:03:01 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:59 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:57 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:52 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-17 19:02:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:37 | Yaka Wewa (Ma Oya) | 1.64 | 🟢 Normal | -0.021 |  |
| 2025-12-17 19:02:14 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 19:01:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:33 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:28 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 19:01:08 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:00:47 | Horowpothana (Yan Oya) | 5.74 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 19:04:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 19:07:28 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-17 19:03:22 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 19:06:11 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 19:02:14 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 19:07:42 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 19:04:28 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 19:01:28 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 19:04:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 19:05:44 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 19:08:54 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:04:52 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:04:26 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:57 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:33 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:05:55 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:08 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:01:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:06:58 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:41 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:03:01 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:02:59 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:07:47 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:08:00 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:05:56 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:06:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 19:47:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.006 |  |
| 2025-12-17 19:02:52 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-17 19:00:47 | Horowpothana (Yan Oya) | 5.74 | 🟢 Normal | -0.011 |  |
| 2025-12-17 19:04:43 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-17 19:02:37 | Yaka Wewa (Ma Oya) | 1.64 | 🟢 Normal | -0.021 |  |
| 2025-12-17 19:06:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2025-12-17 18:02:26 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.030 |  |
| 2025-12-17 19:26:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)