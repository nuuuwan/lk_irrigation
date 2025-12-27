# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_23:23:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,671 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 23:23:28 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.008 |  |
| 2025-12-27 23:22:33 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:10:48 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:09:19 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:06:57 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 23:05:29 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-27 23:04:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2025-12-27 23:04:43 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 23:04:25 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 23:04:23 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-27 23:04:15 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:03:51 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2025-12-27 23:03:29 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:03:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:45 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-27 23:02:01 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 23:01:52 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2025-12-27 23:01:49 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 23:01:42 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-27 23:01:37 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.005 |  |
| 2025-12-27 23:01:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:01:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:01:22 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-27 23:00:57 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:00:32 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-27 22:43:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 22:03:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2025-12-27 23:02:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-27 23:00:32 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-27 23:04:25 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 23:04:43 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-27 23:01:22 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-27 23:01:49 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 23:02:01 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 23:06:57 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:54 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:03:29 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:02:06 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:10:48 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:33 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:09:19 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:18:12 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:04:15 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:01:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:03:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:02:45 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:00:57 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:22:33 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:09:15 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:01:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 23:01:37 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.005 |  |
| 2025-12-27 23:23:28 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.008 |  |
| 2025-12-27 23:05:29 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 23:01:42 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:08:01 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2025-12-27 23:04:23 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-27 23:01:52 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2025-12-27 23:04:43 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2025-12-27 23:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)