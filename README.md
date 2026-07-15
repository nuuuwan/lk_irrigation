# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_20:18:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,186 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 20:18:42 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-07-15 20:13:44 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:12:29 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.079 |  |
| 2026-07-15 20:09:46 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:09:34 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:09:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:08:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:05:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:05:20 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:04:40 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 20:04:28 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-07-15 20:04:25 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:04:14 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:43 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:03:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:30 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.146 |  |
| 2026-07-15 20:03:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:00 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:02:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-07-15 20:02:47 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.077 |  |
| 2026-07-15 20:02:31 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:02:15 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:02:10 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:52 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:51 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:44 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:38 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:38 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-07-15 20:01:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.064 |  |
| 2026-07-15 20:01:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:15 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:00:50 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:00:25 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 19:38:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 20:02:48 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-07-15 20:04:40 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 20:02:10 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:44 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:52 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:08:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:09:46 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:02:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 19:38:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:00 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:00:50 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:13:44 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:51 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:02:31 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:01:38 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:04:14 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:05:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:04:25 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:09:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:05:20 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:00:25 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 20:18:42 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-07-15 18:14:35 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-07-15 20:03:43 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:09:34 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:02:15 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:01:15 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-15 20:01:38 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-07-15 20:04:28 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-07-15 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.062 |  |
| 2026-07-15 20:01:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.064 |  |
| 2026-07-15 20:02:47 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.077 |  |
| 2026-07-15 20:12:29 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.079 |  |
| 2026-07-15 20:03:30 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)