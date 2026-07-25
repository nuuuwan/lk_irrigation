# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_14:15:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,904 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 14:15:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:14:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:09:14 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:07:57 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:07:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-07-25 14:07:12 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-07-25 14:06:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:06:16 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:05:33 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:04:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:07 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:03 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:03 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:02 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:03:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.089 |  |
| 2026-07-25 14:03:34 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:03:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-25 14:03:10 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:37 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-07-25 14:02:33 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-25 14:02:32 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:27 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-07-25 14:02:11 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-25 14:01:49 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:45 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.051 |  |
| 2026-07-25 14:01:43 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:01:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:00 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-25 14:01:00 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:38 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:36 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 14:02:33 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-25 14:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-25 14:03:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-25 14:01:00 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-25 14:02:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:36 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:11 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:38 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:03 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:49 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:07:57 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:02:32 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:06:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:14:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:07 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:01:00 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:03 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:05:33 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:15:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:03:10 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:03:34 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:09:14 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:00:29 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:04:02 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-25 14:07:12 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-07-25 14:06:16 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:04:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:02:27 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:01:43 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-25 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-07-25 14:02:37 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-07-25 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.030 |  |
| 2026-07-25 14:07:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-07-25 14:01:45 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.051 |  |
| 2026-07-25 14:03:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)