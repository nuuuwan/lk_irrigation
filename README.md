# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_19:15:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 19:15:21 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:14:57 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:14:27 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:12:35 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 19:08:30 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 19:07:01 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 19:06:51 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | -0.086 |  |
| 2026-06-07 19:05:38 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.048 |  |
| 2026-06-07 19:05:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:35 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:35 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:31 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.203 |  |
| 2026-06-07 19:04:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:13 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 19:00:33 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-07 19:02:36 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-07 19:07:01 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 19:02:53 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-07 19:03:03 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 19:02:19 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 19:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 19:08:30 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 19:03:49 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 19:12:35 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:14:57 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:15:21 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 19:04:13 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:01:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:35 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:35 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:19 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:05:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:01:57 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:04:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:02:15 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:02:10 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:14:27 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:03:23 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:02:55 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:03:07 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 19:01:43 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-06-07 19:02:19 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-06-07 19:03:22 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-06-07 19:05:38 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.048 |  |
| 2026-06-07 19:02:24 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 19:06:51 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | -0.086 |  |
| 2026-06-07 19:04:31 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.203 |  |
| 2026-06-07 19:03:45 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.846 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)