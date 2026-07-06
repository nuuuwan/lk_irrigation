# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_19:14:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 19:14:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:11:07 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 19:10:25 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.044 |  |
| 2026-07-06 19:08:54 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:08:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-06 19:08:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.044 |  |
| 2026-07-06 19:08:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:08:06 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:05:38 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:04:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-06 19:04:53 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.059 |  |
| 2026-07-06 19:04:28 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-07-06 19:03:22 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:03:00 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-07-06 19:02:41 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:02:36 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:34 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.013 |  |
| 2026-07-06 19:01:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:01:33 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:01:25 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:00:36 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:16 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:59:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:59:34 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-07-06 18:42:36 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 19:03:00 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-07-06 19:04:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-06 19:11:07 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-06 19:08:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-06 19:00:16 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:59:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:36 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:01:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:02:43 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:08:42 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:34 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:01:30 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:03:22 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:38 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:00:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:08:54 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:01:25 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:05:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:14:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:01:33 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:02:36 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 19:08:06 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:02:41 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:08:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-07-06 19:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:59:34 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-07-06 19:02:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.013 |  |
| 2026-07-06 19:04:28 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-07-06 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.041 |  |
| 2026-07-06 19:08:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.044 |  |
| 2026-07-06 19:10:25 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.044 |  |
| 2026-07-06 19:04:53 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)