# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_20:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 20:17:22 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:12:48 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.017 |  |
| 2026-01-03 20:10:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:10:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:09:57 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:09:07 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:08:22 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:08:17 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:07:54 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-01-03 20:07:46 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.035 |  |
| 2026-01-03 20:07:29 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.009 |  |
| 2026-01-03 20:06:46 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-01-03 20:06:23 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:05:38 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:05:05 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:04:43 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:17 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:13 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:13 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:03:59 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-03 20:03:23 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-01-03 20:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 20:02:37 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-01-03 20:02:27 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:02:19 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:02:14 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-03 20:02:04 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:01:56 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:55 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-03 20:01:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:19 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:13 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 20:00:22 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-01-03 20:03:59 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-03 20:01:55 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-03 20:02:14 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-03 20:01:13 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 20:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 20:00:22 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:56 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:08:22 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:09:57 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:02:19 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:13 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:19 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:01:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:17 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:05:38 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:06:23 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:10:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:03:23 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:13 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:08:17 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:04:43 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:09:07 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:10:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-03 20:07:29 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.009 |  |
| 2026-01-03 20:17:22 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:02:04 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:05:05 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:02:27 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-03 20:12:48 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.017 |  |
| 2026-01-03 20:06:46 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-01-03 20:02:37 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-01-03 20:07:54 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-01-03 20:07:46 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.035 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)