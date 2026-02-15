# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_06:18:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 06:18:42 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.083 |  |
| 2026-02-15 06:14:58 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.027 |  |
| 2026-02-15 06:13:57 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-15 06:10:51 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:09:39 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:09:02 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-15 06:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-15 06:06:19 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-02-15 06:05:40 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-02-15 06:05:23 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-15 06:05:20 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:05:18 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:57 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-02-15 06:04:41 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-02-15 06:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 06:03:40 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -12.857 |  |
| 2026-02-15 06:03:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-02-15 06:03:26 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -12.857 |  |
| 2026-02-15 06:02:57 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:56 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-02-15 06:02:44 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:44 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-02-15 06:02:36 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-15 06:02:20 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.141 |  |
| 2026-02-15 06:02:10 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:04 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.301 |  |
| 2026-02-15 06:01:49 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:01:32 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-15 06:01:20 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.029 |  |
| 2026-02-15 06:01:19 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:01:13 | Manampitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-02-15 06:01:09 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.845 | 🔺 Rising |
| 2026-02-15 06:00:14 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-02-15 06:00:06 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-02-15 05:58:05 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.301 |  |
| 2026-02-15 05:57:36 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.845 | 🔺 Rising |
| 2026-02-15 05:35:25 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.083 |  |
| 2026-02-15 05:32:38 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 06:01:09 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.845 | 🔺 Rising |
| 2026-02-15 06:02:44 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-02-15 06:01:13 | Manampitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-02-15 06:09:02 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-02-15 06:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-15 06:13:57 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-15 06:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 06:05:23 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-15 06:09:39 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:10 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:05:18 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:44 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:02:57 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:28 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:04:41 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:05:20 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:01:49 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:10:51 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:32:38 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:01:19 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 06:01:32 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-15 06:02:36 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-15 06:06:19 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-02-15 06:14:58 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.027 |  |
| 2026-02-15 06:00:06 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-02-15 06:04:57 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.028 |  |
| 2026-02-15 06:05:40 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-02-15 06:01:20 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.029 |  |
| 2026-02-15 06:02:56 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-02-15 06:03:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-02-15 06:04:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-02-15 06:18:42 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.083 |  |
| 2026-02-15 06:00:14 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-02-15 06:02:20 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.141 |  |
| 2026-02-15 06:02:04 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.301 |  |
| 2026-02-15 06:03:40 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -12.857 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)