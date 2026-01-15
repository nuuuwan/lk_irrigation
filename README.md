# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_13:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 13:11:11 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-15 13:09:23 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:09:07 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:09:06 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-15 13:07:23 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.138 |  |
| 2026-01-15 13:06:51 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:06:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-01-15 13:06:28 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 13:06:20 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-01-15 13:05:56 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-01-15 13:05:37 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:05:03 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.038 |  |
| 2026-01-15 13:04:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:04:01 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:46 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:40 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-15 13:03:31 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 13:03:25 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-01-15 13:03:08 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:57 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:02:17 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 13:02:03 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-01-15 13:02:00 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:57 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:48 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 13:01:47 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.051 |  |
| 2026-01-15 13:01:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:00:56 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:00:24 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:00:20 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 12:12:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-15 13:11:11 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-15 13:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-15 13:03:31 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-15 13:01:48 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 13:06:28 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 13:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 13:02:00 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:00:20 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:09:23 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:57 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:04:01 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:05:37 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:09:06 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:03:46 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:01:47 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:06:51 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:09:07 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 13:06:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-01-15 13:06:20 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-01-15 13:02:17 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:03:08 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:00:56 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:04:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:00:24 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:57 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:02:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-15 13:03:40 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-01-15 13:05:56 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-01-15 13:02:03 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-01-15 13:03:25 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-01-15 12:07:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.038 |  |
| 2026-01-15 13:05:03 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.038 |  |
| 2026-01-15 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.051 |  |
| 2026-01-15 13:07:23 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)