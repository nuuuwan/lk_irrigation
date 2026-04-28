# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_22:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 22:19:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 22:15:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.036 |  |
| 2026-04-28 22:13:59 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:13:22 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-28 22:08:50 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.048 |  |
| 2026-04-28 22:07:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:07:26 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:07:01 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.018 |  |
| 2026-04-28 22:06:55 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:06:39 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.041 |  |
| 2026-04-28 22:06:06 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 22:05:36 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:32 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-28 22:03:59 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 22:03:48 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 22:03:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:03:23 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:03:02 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-04-28 22:03:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-04-28 22:02:50 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:02:40 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-28 22:02:30 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:02:12 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:02:04 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:02:00 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:00:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 22:04:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 22:06:06 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 22:03:48 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 22:00:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 22:03:59 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 22:19:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-28 22:02:04 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:03:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:02:30 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:13:59 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:07:26 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:07:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:32 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:05:36 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:06:55 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 20:07:27 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:07:00 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:13:22 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-28 22:02:50 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:03:23 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:02:12 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:02:00 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:01:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:07:01 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.018 |  |
| 2026-04-28 22:02:40 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-28 22:03:02 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-04-28 22:15:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.036 |  |
| 2026-04-28 22:06:39 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.041 |  |
| 2026-04-28 22:03:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-04-28 21:07:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.042 |  |
| 2026-04-28 22:08:50 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.048 |  |
| 2026-04-28 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)