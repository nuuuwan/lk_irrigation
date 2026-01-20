# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_16:09:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 16:09:20 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.054 |  |
| 2026-01-20 16:07:36 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:07:31 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:06:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:05:58 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-20 16:05:51 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-01-20 16:05:23 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:05:03 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2026-01-20 16:04:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-01-20 16:03:55 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:28 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-20 16:03:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:01 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:01 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:53 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:46 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.038 |  |
| 2026-01-20 16:02:32 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:25 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-20 16:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:01:55 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:53 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:34 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:24 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:09 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:01:09 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:03 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.030 |  |
| 2026-01-20 16:01:03 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-20 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:00:07 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-20 15:16:50 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.559 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 15:16:50 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-01-20 16:05:58 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-20 15:01:54 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-20 16:02:25 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-20 16:01:03 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-20 16:03:28 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-20 16:01:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:11 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:09 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:34 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 15:05:19 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 15:06:19 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:01 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:01 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:07:36 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 15:08:22 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:03:55 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:04:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:53 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:03 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:32 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:06:13 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:53 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:55 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:05:23 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:01:24 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:07:31 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 16:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:01:09 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:00:07 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-20 16:03:57 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-01-20 16:05:51 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-01-20 16:01:03 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.030 |  |
| 2026-01-20 16:02:46 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.038 |  |
| 2026-01-20 16:09:20 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.054 |  |
| 2026-01-20 16:05:03 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2026-01-20 15:06:28 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -1.023 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)