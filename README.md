# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_13:16:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 13:16:17 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:12:28 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:12:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-16 13:11:00 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:10:02 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:07:52 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:42 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:19 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:07:05 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 13:04:57 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:04:56 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-16 13:04:51 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.070 |  |
| 2026-04-16 13:04:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:04:31 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:34 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:34 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:27 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:24 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.072 |  |
| 2026-04-16 13:03:19 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:14 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:06 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-16 13:02:49 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:02:38 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.119 |  |
| 2026-04-16 13:02:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:02:30 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-04-16 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-04-16 13:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:01:33 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:01:21 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:01:20 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:00:42 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-04-16 13:00:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:00:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 13:02:30 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-04-16 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-16 13:04:56 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-16 13:07:05 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 13:00:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:34 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:04:57 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:42 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:14 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:04:31 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:01:20 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:02:49 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:16:17 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:04:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-16 12:08:04 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:03:27 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:07:52 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:12:28 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-16 13:11:00 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:10:02 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:07:19 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-04-16 13:03:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:19 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:06 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:03:34 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:01:33 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:02:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:01:21 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-16 13:00:42 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-04-16 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-04-16 13:12:07 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-16 13:04:51 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.070 |  |
| 2026-04-16 13:00:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.072 |  |
| 2026-04-16 13:03:24 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.072 |  |
| 2026-04-16 13:02:38 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)