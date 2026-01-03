# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_03:11:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 03:11:55 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:11:02 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.026 |  |
| 2026-01-04 03:08:36 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:08:35 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:08:34 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.043 |  |
| 2026-01-04 03:06:38 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-04 03:06:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 03:05:24 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:05:23 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 03:05:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-01-04 03:04:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-01-04 03:04:30 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-01-04 03:04:17 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:12 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:02 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-04 03:03:52 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-04 03:03:42 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.339 |  |
| 2026-01-04 03:03:24 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:03:11 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:02:47 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.005 |  |
| 2026-01-04 03:02:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-04 03:02:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.158 |  |
| 2026-01-04 03:02:03 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 03:01:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:01:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:35:32 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-04 02:33:28 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:33:10 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:32:51 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:32:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-04 02:25:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.026 |  |
| 2026-01-04 02:24:51 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.026 |  |
| 2026-01-04 02:21:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:19:34 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 8.842 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-04 02:19:34 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 8.842 | 🔺 Rising |
| 2026-01-04 03:05:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-01-04 03:04:39 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-01-04 03:02:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-04 03:06:38 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-04 03:03:52 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-04 02:32:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-04 02:35:32 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-04 03:02:03 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-04 03:05:23 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 03:06:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 02:01:12 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-04 03:03:11 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:33:28 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:17 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:21:34 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:01:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:11:55 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:05:24 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:30 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:04:12 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:08:36 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:07:53 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:27 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 03:02:47 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.005 |  |
| 2026-01-04 03:04:02 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-04 03:01:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-01-03 23:00:29 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-01-04 03:04:30 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-01-04 03:11:02 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.026 |  |
| 2026-01-04 03:08:34 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.043 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-04 03:02:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.158 |  |
| 2026-01-04 03:03:42 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.339 |  |
| 2026-01-04 02:08:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)