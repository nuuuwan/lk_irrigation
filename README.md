# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_21:41:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 21:41:37 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:30:08 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:29:41 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:18:12 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-31 21:12:23 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:09:09 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:08:26 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-31 21:07:41 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:06:08 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:05:46 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:42 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:25 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:25 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:04:51 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:04:33 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:04:31 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-31 21:04:27 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-01-31 21:03:51 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.330 |  |
| 2026-01-31 21:03:46 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:03:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:03:19 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:03:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-31 21:03:08 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:02:56 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 21:02:49 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-31 21:02:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:44 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-31 21:02:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:07 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:33 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.038 |  |
| 2026-01-31 21:01:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:19 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:18 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:00:53 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-31 21:00:27 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 21:04:27 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-01-31 21:03:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-31 21:02:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-31 21:02:49 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-31 21:18:12 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-31 21:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 21:08:26 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-31 21:00:53 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-31 21:04:51 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:03:19 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:03:08 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 21:00:27 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:41:37 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:03:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:03:46 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:12:23 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:42 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:07:41 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:18 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:07 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:49 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:46 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:25 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:09:09 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:02:56 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:30:08 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:19 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:05:25 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:06:08 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:04:33 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-31 21:04:31 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-31 21:01:33 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.038 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-01-31 21:03:51 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.330 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)