# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_07:22:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,555 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 07:22:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.015 |  |
| 2026-05-03 07:15:04 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-05-03 07:13:56 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-03 07:13:56 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.014 |  |
| 2026-05-03 07:13:50 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-03 07:13:26 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:12:14 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-03 07:09:46 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:09:42 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:07:56 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:07:54 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:06:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.036 |  |
| 2026-05-03 07:06:25 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.022 |  |
| 2026-05-03 07:06:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:06:04 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-03 07:05:42 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:05:15 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 07:05:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.109 |  |
| 2026-05-03 07:05:01 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-03 07:04:43 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-05-03 07:04:09 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:04:02 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.348 |  |
| 2026-05-03 07:03:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-05-03 07:03:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:03:17 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-03 07:03:03 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-05-03 07:03:00 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-05-03 07:02:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:46 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:17 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:01:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-03 07:01:42 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-03 07:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-03 07:01:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 07:01:13 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 07:00:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -6.701 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 07:05:01 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-03 06:07:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-03 07:01:42 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-03 07:06:04 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-03 07:12:14 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-03 07:05:15 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 07:13:56 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-03 07:01:13 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 07:13:50 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-03 07:01:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 07:06:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:09:46 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:09:42 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:07:54 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:04:09 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:03:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:47 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:17 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:05:42 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:07:56 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:13:26 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 07:02:46 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:26:36 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-05-03 07:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-03 07:03:17 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-03 07:13:56 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.014 |  |
| 2026-05-03 07:22:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.015 |  |
| 2026-05-03 07:03:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-05-03 07:03:03 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-05-03 07:01:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-03 07:03:00 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-05-03 07:04:43 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-05-03 07:06:25 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.022 |  |
| 2026-05-03 07:06:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.036 |  |
| 2026-05-03 07:15:04 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-05-03 07:05:04 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.109 |  |
| 2026-05-03 07:04:02 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.348 |  |
| 2026-05-03 07:00:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -6.701 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)