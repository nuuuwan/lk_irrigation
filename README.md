# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_20:22:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 20:22:30 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.008 |  |
| 2026-01-01 20:19:45 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-01 20:11:25 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 20:11:04 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-01 20:09:39 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:08:26 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 20:08:18 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-01-01 20:07:37 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-01 20:07:36 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-01 20:07:18 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:06:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:06:15 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:06:15 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2026-01-01 20:05:58 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-01 20:05:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-01 20:05:53 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 20:05:14 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:05:08 | Katharagama (Menik Ganga) | 1.34 | 🟢 Normal | 0.854 | 🔺 Rising |
| 2026-01-01 20:05:04 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:03:45 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:03:41 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 20:03:30 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:03:25 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 20:03:21 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:12 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:03:05 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:02:37 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:02:20 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-01-01 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:01:55 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-01 20:01:39 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:01:32 | Horowpothana (Yan Oya) | 3.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:01:23 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 20:05:08 | Katharagama (Menik Ganga) | 1.34 | 🟢 Normal | 0.854 | 🔺 Rising |
| 2026-01-01 20:01:55 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.367 | 🔺 Rising |
| 2026-01-01 20:19:45 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-01 20:05:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-01 20:03:41 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 20:05:58 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-01 20:07:36 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-01 20:03:25 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 20:05:04 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:01:32 | Horowpothana (Yan Oya) | 3.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 20:11:25 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 20:08:26 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-01 20:11:04 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-01 20:05:53 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 20:01:39 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:16 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:09:39 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:12 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:07:18 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:03:21 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:06:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-01 20:22:30 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.008 |  |
| 2026-01-01 20:07:37 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-01 20:06:15 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2026-01-01 20:03:45 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:03:05 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:06:15 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:05:14 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-01 20:01:23 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-01-01 20:08:18 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-01-01 20:03:30 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:02:37 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:02:20 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)