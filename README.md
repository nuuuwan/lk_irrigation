# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_17:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,257 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 17:11:15 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:10:30 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2026-01-07 17:10:12 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-01-07 17:08:22 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:58 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:51 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:47 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-01-07 17:06:38 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-01-07 17:06:24 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-01-07 17:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-01-07 17:06:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-07 17:06:11 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:05:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-01-07 17:04:36 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:04:30 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:04:10 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:04:05 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:03:59 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:03:49 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-07 17:03:33 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:03:20 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 17:03:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.025 |  |
| 2026-01-07 17:02:57 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-01-07 17:02:26 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:02:09 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-01-07 17:02:09 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:04 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:01:54 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-01-07 17:01:51 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:01:15 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:00:54 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:00:17 | Siyambalanduwa (Heda Oya) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-01-07 17:00:13 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-07 16:39:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 17:02:09 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-01-07 17:06:38 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-01-07 17:00:13 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-07 17:06:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-07 17:03:49 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-07 17:03:20 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 17:01:51 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 17:01:15 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:09 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:04:30 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:11 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:11:15 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:51 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:06:02 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:38 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:06:58 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:04:10 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:02:26 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:08:22 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-07 17:10:12 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-01-07 16:08:30 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:02:04 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:03:59 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:04:36 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 17:06:24 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-01-07 17:06:47 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-01-07 17:04:05 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:03:33 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-01-07 17:03:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.025 |  |
| 2026-01-07 17:05:32 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-01-07 17:01:54 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-01-07 17:10:30 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2026-01-07 17:02:57 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-01-07 17:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-01-07 17:00:17 | Siyambalanduwa (Heda Oya) | 1.55 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)