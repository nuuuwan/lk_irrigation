# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_06:13:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 06:13:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:11:53 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.106 |  |
| 2026-07-21 06:11:36 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:11:03 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:09:37 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-21 06:09:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:08:48 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:07:27 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:07:20 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:06:13 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:06:05 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:06:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:05:58 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.005 |  |
| 2026-07-21 06:05:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:04:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:04:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:04:03 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | -0.072 |  |
| 2026-07-21 06:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:03:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.084 |  |
| 2026-07-21 06:03:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:03:04 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:36 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:25 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:21 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 06:02:13 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:59 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:01:49 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:37 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:28 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-21 06:01:18 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 06:01:11 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:00:40 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:00:33 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 1.044 | 🔺 Rising |
| 2026-07-21 06:00:30 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.036 |  |
| 2026-07-21 06:00:11 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-21 05:57:01 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-21 05:57:00 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-21 05:56:09 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.084 |  |
| 2026-07-21 05:35:01 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 06:00:33 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 1.044 | 🔺 Rising |
| 2026-07-21 06:02:21 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 06:09:37 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-21 06:00:11 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-21 06:01:28 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-21 06:01:18 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 06:05:58 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.005 |  |
| 2026-07-21 06:01:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:25 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:11 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:11:03 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:07:27 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:49 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:36 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:08:48 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:04:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:05:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:03:13 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:09:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:06:13 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:06:01 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:02:13 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:11:36 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:04:20 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:13:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-07-21 06:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:07:20 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:01:59 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:00:40 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-21 06:00:30 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.036 |  |
| 2026-07-21 06:04:03 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | -0.072 |  |
| 2026-07-21 06:03:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.084 |  |
| 2026-07-21 06:11:53 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)