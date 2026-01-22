# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_07:22:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 07:22:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:14:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:14:07 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-22 07:13:46 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-22 07:13:35 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.053 |  |
| 2026-01-22 07:11:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-22 07:08:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.116 |  |
| 2026-01-22 07:07:58 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:07:33 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:32 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:12 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:08 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.048 |  |
| 2026-01-22 07:06:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-22 07:05:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:05:13 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:04:18 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:04:06 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-01-22 07:03:23 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-22 07:03:22 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:03:20 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-22 07:02:54 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-22 07:02:48 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:02:19 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.175 |  |
| 2026-01-22 07:01:32 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:29 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.023 |  |
| 2026-01-22 07:01:25 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:22 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.094 |  |
| 2026-01-22 07:01:20 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-22 07:01:18 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:11 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-22 07:00:55 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 07:00:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:00:22 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:00:18 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-22 06:39:25 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-01-22 06:37:09 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 07:03:20 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-22 07:01:11 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-22 07:03:23 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-22 07:14:07 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-22 07:00:55 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 07:01:25 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:32 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:00:18 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:12 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:18 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 06:09:45 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:22:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:01:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:14:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 06:03:27 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:02:19 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:00:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:00:22 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:02:48 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:07:33 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:03:22 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:05:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:06:32 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:04:06 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 06:13:49 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:04:18 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:07:58 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-22 07:13:46 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-22 07:01:20 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-22 07:02:54 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-22 07:06:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-22 07:01:29 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.023 |  |
| 2026-01-22 07:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-01-22 07:06:08 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.048 |  |
| 2026-01-22 07:13:35 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.053 |  |
| 2026-01-22 07:11:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.070 |  |
| 2026-01-22 07:01:22 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.094 |  |
| 2026-01-22 07:08:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.116 |  |
| 2026-01-22 07:01:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)