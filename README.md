# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_22:09:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 22:09:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2025-12-22 22:09:07 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:55 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:07:47 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:07:43 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:06:28 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2025-12-22 22:06:13 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:06:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:58 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-22 22:05:55 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:44 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:05:43 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:42 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 22:04:28 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:04:28 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-22 22:03:18 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:03:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:03:10 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:02:20 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:02:14 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2025-12-22 22:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:53 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:36 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.025 |  |
| 2025-12-22 22:01:34 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:01:19 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2025-12-22 22:01:14 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:09 | Horowpothana (Yan Oya) | 3.19 | 🟢 Normal | -0.030 |  |
| 2025-12-22 21:35:33 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-22 21:23:52 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-22 21:18:43 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.059 |  |
| 2025-12-22 21:16:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:16:12 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:12:43 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 21:00:37 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-22 22:05:58 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-22 21:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-22 22:08:55 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-22 22:04:28 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-22 22:05:42 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 22:01:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:19 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:09:07 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:02:20 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:06:13 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:16:13 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:55 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:04:28 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:07:47 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:06:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:14 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:43 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:07:43 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 21:03:31 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:01:53 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:03:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:05:44 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:03:10 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:01:34 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:03:18 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:06:28 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2025-12-22 22:01:36 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.025 |  |
| 2025-12-22 21:05:32 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2025-12-22 22:02:14 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.029 |  |
| 2025-12-22 22:01:09 | Horowpothana (Yan Oya) | 3.19 | 🟢 Normal | -0.030 |  |
| 2025-12-22 22:01:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2025-12-22 22:09:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)