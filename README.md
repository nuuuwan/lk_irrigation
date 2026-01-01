# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_09:34:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,575 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 09:34:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-01-01 09:19:45 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 09:19:17 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:15:36 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-01 09:14:18 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-01 09:12:51 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.034 |  |
| 2026-01-01 09:12:34 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-01 09:11:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:11:11 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:11:03 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:08:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:07:58 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.014 |  |
| 2026-01-01 09:06:33 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:06:16 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-01 09:06:01 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-01 09:05:40 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:04:56 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.032 |  |
| 2026-01-01 09:04:52 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-01 09:04:19 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:04:14 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-01 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.159 |  |
| 2026-01-01 09:03:51 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.033 |  |
| 2026-01-01 09:03:45 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:03:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-01-01 09:03:33 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-01-01 09:03:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.132 |  |
| 2026-01-01 09:02:50 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 09:02:39 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-01 09:02:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-01 09:02:04 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:02:01 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:01:56 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 09:01:35 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:01:07 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 09:00:59 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.043 |  |
| 2026-01-01 09:00:23 | Nakkala (Kumbukkan Oya) | 0.23 | 🟢 Normal | -1.012 |  |
| 2026-01-01 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 09:06:01 | Peradeniya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-01 09:04:52 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-01 09:02:39 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-01 09:15:36 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-01 09:02:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-01 09:01:35 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-01 09:01:07 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 09:06:16 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-01 09:19:45 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-01 09:02:50 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 09:01:56 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 09:14:18 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-01 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:08:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:11:03 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:06:33 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:03:45 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:11:11 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:05:40 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:19:17 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:11:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-01 09:12:34 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-01 09:04:19 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 08:05:52 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:02:01 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:02:04 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-01 09:07:58 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.014 |  |
| 2026-01-01 09:03:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-01-01 09:04:14 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-01 09:34:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-01-01 09:03:33 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-01-01 09:04:56 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.032 |  |
| 2026-01-01 09:03:51 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.033 |  |
| 2026-01-01 09:12:51 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.034 |  |
| 2026-01-01 09:00:59 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.043 |  |
| 2026-01-01 09:03:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.132 |  |
| 2026-01-01 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.159 |  |
| 2026-01-01 09:00:23 | Nakkala (Kumbukkan Oya) | 0.23 | 🟢 Normal | -1.012 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)