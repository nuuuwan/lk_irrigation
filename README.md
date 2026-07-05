# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_18:09:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,151 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 18:09:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:07:23 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:07:11 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:39 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:38 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:38 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-07-05 18:05:37 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:05:37 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:35 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:30 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.032 |  |
| 2026-07-05 18:05:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:04:54 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-05 18:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-07-05 18:04:19 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 18:04:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:04:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:33 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.021 |  |
| 2026-07-05 18:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.025 |  |
| 2026-07-05 18:03:25 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:02:50 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.059 |  |
| 2026-07-05 18:02:46 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.082 |  |
| 2026-07-05 18:02:44 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 18:02:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:02:24 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 18:02:20 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-07-05 18:01:53 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:01:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:01:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:01:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.047 |  |
| 2026-07-05 18:01:14 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.051 |  |
| 2026-07-05 18:00:49 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-07-05 18:00:33 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:00:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:00:11 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 18:04:54 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-05 18:00:11 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-05 18:02:44 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 18:04:19 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 18:02:24 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 18:00:33 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:01:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:04:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:00:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:01:53 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:09:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:07:23 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:04:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:11:23 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:37 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:02:33 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 16:02:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:01:33 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:49 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-07-05 18:05:38 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-07-05 18:03:25 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-07-05 18:03:33 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.021 |  |
| 2026-07-05 18:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.025 |  |
| 2026-07-05 17:07:15 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-07-05 18:05:30 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.032 |  |
| 2026-07-05 18:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-07-05 18:01:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.047 |  |
| 2026-07-05 18:01:14 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.051 |  |
| 2026-07-05 18:02:20 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-07-05 18:02:50 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.059 |  |
| 2026-07-05 18:02:46 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)