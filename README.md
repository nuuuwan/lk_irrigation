# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_16:19:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 16:19:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:13:12 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.027 |  |
| 2026-04-20 16:12:16 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 16:07:55 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:07:50 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 16:07:24 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-20 16:06:49 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:06:28 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:06:14 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-04-20 16:05:50 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:05:36 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-20 16:05:14 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-20 16:05:13 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-20 16:04:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:42 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-20 16:04:28 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:18 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:04:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:04:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:59 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:03:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:40 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 16:03:03 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-20 16:03:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-20 16:02:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:02:39 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.109 |  |
| 2026-04-20 16:02:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-20 16:02:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:01:45 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-04-20 16:01:38 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.030 |  |
| 2026-04-20 16:01:25 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:01:22 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:01:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:00:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.150 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 16:05:14 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-04-20 16:01:45 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-04-20 16:03:03 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-20 16:05:36 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-20 16:07:24 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-20 16:12:16 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-20 16:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-20 15:03:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-20 16:03:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-20 16:07:50 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 16:03:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 16:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:06:49 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:07:55 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-20 16:04:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:05:50 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:01:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:01:25 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:09:37 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:18 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:19:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:04:28 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:06:28 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:02:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:01:22 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:40 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-20 16:03:59 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:04:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:02:16 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-20 16:04:42 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-20 16:13:12 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.027 |  |
| 2026-04-20 16:06:14 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-04-20 16:01:38 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.030 |  |
| 2026-04-20 16:02:39 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.109 |  |
| 2026-04-20 16:00:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)