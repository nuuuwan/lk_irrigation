# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_14:46:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,556 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 14:46:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-20 14:15:05 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-20 14:09:07 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:08:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:07:57 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:07:19 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:07:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-03-20 14:06:22 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:05:04 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.012 |  |
| 2026-03-20 14:04:52 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:04:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:49 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:42 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.025 |  |
| 2026-03-20 14:04:37 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-03-20 14:04:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:20 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.038 |  |
| 2026-03-20 14:03:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:03:40 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-03-20 14:03:27 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-03-20 14:03:07 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:03:06 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-20 14:02:48 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:39 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 14:02:34 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:33 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.061 |  |
| 2026-03-20 14:02:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-20 14:02:17 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 14:01:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-20 14:15:05 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-20 14:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-20 14:02:39 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 14:46:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-20 14:01:55 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:00:37 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:48 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:07:57 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:00:35 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:03:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:37 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:34 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:02:17 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:04:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:06:22 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:00:54 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:07:19 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:08:50 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:09:07 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:04:52 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:03:07 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-20 14:01:43 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-03-20 14:00:30 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-03-20 14:03:27 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-03-20 14:05:04 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.012 |  |
| 2026-03-20 14:07:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-03-20 14:03:06 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-20 14:04:42 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.025 |  |
| 2026-03-20 14:01:53 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.030 |  |
| 2026-03-20 14:03:40 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-03-20 14:04:20 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.038 |  |
| 2026-03-20 14:04:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-03-20 14:02:33 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.061 |  |
| 2026-03-20 14:01:22 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)