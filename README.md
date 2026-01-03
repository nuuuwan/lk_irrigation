# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_21:33:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 21:33:14 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-03 21:22:58 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-01-03 21:13:23 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-03 21:11:56 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -18.000 |  |
| 2026-01-03 21:11:54 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -18.000 |  |
| 2026-01-03 21:11:51 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 21:10:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:08:42 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:40 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:34 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:08:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:14 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:07:56 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:07:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:07:47 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:07:43 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:05:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.068 |  |
| 2026-01-03 21:05:38 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-03 21:05:22 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:04:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-03 21:03:56 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:51 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-01-03 21:03:43 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:03:19 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:19 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:03:11 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-03 21:03:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:04 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:02:56 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-01-03 21:02:49 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:02:44 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:02:35 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:02:00 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.220 |  |
| 2026-01-03 21:01:53 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:01:43 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.025 |  |
| 2026-01-03 21:01:25 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:01:02 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-03 21:03:51 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-01-03 21:05:38 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-03 21:04:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-03 21:03:11 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-03 21:13:23 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-03 21:01:02 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 21:11:51 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 21:33:14 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-03 21:07:43 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:56 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:01:25 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:19 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:03:04 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:02:44 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:42 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:40 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:07:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:07:56 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:08:14 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-03 21:02:49 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:08:34 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:02:35 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:10:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:03:19 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:05:22 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-01-03 21:22:58 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-01-03 21:03:43 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:07:47 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:01:53 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-01-03 21:02:56 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-01-03 21:01:43 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.025 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 21:05:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.068 |  |
| 2026-01-03 21:02:00 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.220 |  |
| 2026-01-03 21:11:56 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)