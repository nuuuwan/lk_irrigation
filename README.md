# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_20:17:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 20:17:33 | Thaldena (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-11 20:12:12 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 20:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.029 |  |
| 2025-12-11 20:10:18 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 20:09:38 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:09:17 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2025-12-11 20:06:35 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:06:05 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:05:35 | Padiyathalawa (Maduru Oya) | 3.60 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-11 20:05:22 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2025-12-11 20:05:18 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-11 20:04:49 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2025-12-11 20:04:37 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2025-12-11 20:04:28 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-11 20:04:00 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:03:51 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:03:19 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:03:05 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 20:02:42 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:26 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:20 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:02:17 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 20:02:16 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:12 | Horowpothana (Yan Oya) | 4.21 | 🟢 Normal | -0.049 |  |
| 2025-12-11 20:02:11 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:01:51 | Siyambalanduwa (Heda Oya) | 1.80 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-11 20:01:22 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:00:50 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:00:35 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.013 |  |
| 2025-12-11 20:00:15 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:58:11 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:30:45 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 20:09:17 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 20:05:22 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2025-12-11 20:04:37 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2025-12-11 20:17:33 | Thaldena (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-11 20:01:51 | Siyambalanduwa (Heda Oya) | 1.80 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-11 20:05:35 | Padiyathalawa (Maduru Oya) | 3.60 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-11 20:04:28 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-11 20:05:18 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 20:12:12 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 19:04:33 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 20:02:17 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 20:03:05 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 20:10:18 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 20:02:42 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:00:50 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:26 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:16 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 20:02:11 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:00:15 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:09:38 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 19:58:11 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:02:20 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:04:49 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:01:22 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:06:35 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:06:05 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:04:00 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-11 20:03:19 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:03:51 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:00:35 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.013 |  |
| 2025-12-11 19:30:45 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2025-12-11 20:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.029 |  |
| 2025-12-11 20:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 20:02:12 | Horowpothana (Yan Oya) | 4.21 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)