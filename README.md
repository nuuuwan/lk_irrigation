# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_03:35:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,930 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 03:35:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-04-19 03:21:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:15:22 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:12:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:10:13 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.265 |  |
| 2026-04-19 03:08:13 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:08:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:07:57 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.265 |  |
| 2026-04-19 03:07:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-04-19 03:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-19 03:07:06 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-04-19 03:06:50 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-19 03:06:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-19 03:06:47 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-19 03:06:45 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-19 03:05:35 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.005 |  |
| 2026-04-19 03:04:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:04:21 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.038 |  |
| 2026-04-19 03:04:12 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:03:58 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 03:03:43 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:31 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:27 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:14 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:03:01 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.079 |  |
| 2026-04-19 03:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:02:25 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-19 03:01:57 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:01:51 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:01:49 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:01:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.250 |  |
| 2026-04-19 03:01:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 03:06:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-19 03:06:50 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-19 03:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-19 03:00:27 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-19 02:59:44 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-19 03:03:58 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 02:02:51 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-19 03:01:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 03:02:25 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-19 03:04:48 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 02:00:40 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:01:57 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:12:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:01:51 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:21:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:27 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:31 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:03:43 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 02:57:09 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:08:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:15:22 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 02:20:49 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 03:07:06 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-04-19 03:05:35 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.005 |  |
| 2026-04-19 03:08:13 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:04:12 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:03:14 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-19 03:01:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-19 03:07:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-04-19 03:35:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-04-19 03:04:21 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.038 |  |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-19 03:03:01 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.079 |  |
| 2026-04-19 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.250 |  |
| 2026-04-19 03:10:13 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.265 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)