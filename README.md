# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_21:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,116 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 21:12:38 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-10 21:11:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-01-10 21:09:09 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:09:05 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:07:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-01-10 21:06:45 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-01-10 21:06:32 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.032 |  |
| 2026-01-10 21:06:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 21:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:05:56 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-10 21:05:47 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:05:06 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:04:29 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:04:22 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-01-10 21:04:19 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-10 21:04:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-01-10 21:03:27 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 21:03:05 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:58 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:56 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-10 21:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-10 21:02:30 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:29 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-01-10 21:02:10 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:50 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:44 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 21:01:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:18 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-10 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-10 21:00:40 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:00:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:38:05 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:35:25 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 21:01:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-01-10 21:06:45 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-01-10 21:04:19 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-10 21:01:44 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 21:02:56 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-10 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-10 21:06:22 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 21:03:27 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 21:00:12 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:05:47 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:30 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:00:40 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:35:25 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:03:05 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:05:06 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:09:05 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:58 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:50 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-10 20:13:15 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:04:29 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:10 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:09:09 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:18 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:01:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-10 21:02:29 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-01-10 21:12:38 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-10 21:04:22 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 21:05:56 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-10 21:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-01-10 21:04:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-01-10 21:06:32 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.032 |  |
| 2026-01-10 21:11:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-01-10 21:07:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)