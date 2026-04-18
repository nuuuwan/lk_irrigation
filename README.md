# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_14:19:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,465 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 14:19:03 | Urawa (Nilwala Ganga) | -0.80 | 🟢 Normal | -0.611 |  |
| 2026-04-18 14:16:07 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:13:23 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-04-18 14:09:14 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:08:36 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:06:29 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:06:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:05:44 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:59 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-18 14:04:58 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:40 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-04-18 14:04:37 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-18 14:04:34 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.049 |  |
| 2026-04-18 14:04:28 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:04:27 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:40 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:34 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:16 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:02:57 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-18 14:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-04-18 14:02:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:02:34 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:29 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-04-18 14:02:28 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-18 14:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:02:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:01:12 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.295 |  |
| 2026-04-18 14:01:06 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:00:41 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 14:02:28 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-18 14:04:59 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-18 14:01:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-18 14:04:37 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-18 14:02:57 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-18 13:02:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:03:16 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:08:36 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:24 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:34 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:16:07 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:09:14 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 13:03:07 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:40 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:12 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:05:44 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:58 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:00:41 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:27 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:34 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:06:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:06:29 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:13:23 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-04-18 14:01:06 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:02:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:04:28 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-04-18 14:02:29 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-04-18 14:04:40 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-04-18 14:04:34 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.049 |  |
| 2026-04-18 14:01:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.295 |  |
| 2026-04-18 14:19:03 | Urawa (Nilwala Ganga) | -0.80 | 🟢 Normal | -0.611 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)