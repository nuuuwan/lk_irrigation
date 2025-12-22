# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_21:18:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 21:18:43 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.078 |  |
| 2025-12-22 21:16:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:16:12 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:12:43 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:08:24 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-22 21:06:40 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:05:55 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2025-12-22 21:05:32 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2025-12-22 21:05:18 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:05:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:05:10 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-22 21:05:01 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.019 |  |
| 2025-12-22 21:05:00 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:53 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:42 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:26 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:24 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:21 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:04:14 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:04:05 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-22 21:03:38 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:07 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:02:56 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:02:46 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2025-12-22 21:01:47 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:01:26 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:00:59 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.033 |  |
| 2025-12-22 21:00:51 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:00:37 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-22 21:00:29 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:00:23 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2025-12-22 21:00:15 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 21:00:37 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-22 21:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-22 20:03:50 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 21:05:10 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-22 21:00:51 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:26 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:07 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:38 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:16:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:01:26 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:12:43 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:05:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:53 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:08:24 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:08:53 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:05:18 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:05:00 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:42 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 20:07:10 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:24 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:04:14 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:02:56 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:01:47 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:04:21 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:06:40 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2025-12-22 21:05:01 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.019 |  |
| 2025-12-22 21:02:46 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2025-12-22 21:05:55 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2025-12-22 21:00:23 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | -0.021 |  |
| 2025-12-22 21:04:05 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-22 21:05:32 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2025-12-22 21:00:59 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.033 |  |
| 2025-12-22 21:00:15 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.042 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 21:18:43 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.078 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)