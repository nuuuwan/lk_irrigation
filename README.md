# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_04:16:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,967 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 04:16:21 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.065 |  |
| 2026-05-17 04:15:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | -0.571 |  |
| 2026-05-17 04:14:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.571 |  |
| 2026-05-17 04:13:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | -0.571 |  |
| 2026-05-17 04:11:12 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-17 04:09:25 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.098 |  |
| 2026-05-17 04:08:43 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.019 |  |
| 2026-05-17 04:07:46 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-05-17 04:06:41 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 04:05:25 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-17 04:04:54 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:04:53 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:04:15 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 9.474 | 🔺 Rising |
| 2026-05-17 04:03:57 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.039 |  |
| 2026-05-17 04:03:56 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 9.474 | 🔺 Rising |
| 2026-05-17 04:03:55 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.037 |  |
| 2026-05-17 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-05-17 04:03:26 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:03:24 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 04:03:12 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-05-17 04:03:12 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.074 |  |
| 2026-05-17 04:02:40 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:02:35 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-17 04:02:35 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.042 |  |
| 2026-05-17 04:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:02:06 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-17 04:01:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:01:41 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.005 |  |
| 2026-05-17 04:01:39 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:01:29 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:01:11 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | -0.032 |  |
| 2026-05-17 04:01:08 | Moragaswewa (Deduru Oya) | 1.98 | 🟢 Normal | -0.157 |  |
| 2026-05-17 04:00:41 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:38:47 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 04:15:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | -0.571 |  |
| 2026-05-17 02:02:59 | Dunamale (Aththanagalu Oya) | 3.39 | 🟡 Alert | -0.026 |  |
| 2026-05-17 04:04:15 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 9.474 | 🔺 Rising |
| 2026-05-17 04:11:12 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-17 04:06:41 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-17 04:05:25 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 03:04:47 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 04:03:24 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 02:07:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.003 |  |
| 2026-05-17 04:03:26 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:02:40 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:05:46 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:01:29 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 03:01:07 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:01:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:02:12 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 04:01:41 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.005 |  |
| 2026-05-17 04:01:39 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:04:54 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:00:41 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:08:26 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 04:04:53 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:38:47 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.013 |  |
| 2026-05-17 04:08:43 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.019 |  |
| 2026-05-17 04:02:35 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-05-17 04:07:46 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-05-17 04:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-05-17 04:03:12 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 04:01:11 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | -0.032 |  |
| 2026-05-17 04:03:55 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.037 |  |
| 2026-05-17 04:03:57 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.039 |  |
| 2026-05-17 04:02:35 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.042 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 04:16:21 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.065 |  |
| 2026-05-17 04:03:12 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.074 |  |
| 2026-05-17 04:09:25 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.098 |  |
| 2026-05-17 04:01:08 | Moragaswewa (Deduru Oya) | 1.98 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)