# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_21:08:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 21:08:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 21:07:58 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:07:57 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-04-28 21:07:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.042 |  |
| 2026-04-28 21:07:00 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:05:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:05:42 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.049 |  |
| 2026-04-28 21:05:29 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.094 |  |
| 2026-04-28 21:05:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:37 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-28 21:04:29 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 21:03:59 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:03:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 21:03:18 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:03:16 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:02:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 21:02:49 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:02:42 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:02:42 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-04-28 21:02:38 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.022 |  |
| 2026-04-28 21:02:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-04-28 21:02:09 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-04-28 21:02:08 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 21:02:06 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-04-28 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.089 |  |
| 2026-04-28 21:02:04 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 21:01:59 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 21:01:55 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 21:01:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:00:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 21:04:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 21:08:25 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 21:03:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 21:01:59 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 21:01:55 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 21:02:08 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 21:04:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 21:02:04 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 21:04:43 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:03:18 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:37 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:04:29 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:05:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:02:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:03:16 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 20:07:27 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:07:00 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 21:02:42 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:02:49 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:00:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:07:58 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:03:59 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:05:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:01:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-28 21:02:42 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-04-28 21:02:09 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-04-28 21:02:06 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.022 |  |
| 2026-04-28 21:02:38 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.022 |  |
| 2026-04-28 20:18:33 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-04-28 21:07:57 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-04-28 21:02:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-04-28 21:07:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.042 |  |
| 2026-04-28 21:05:42 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.049 |  |
| 2026-04-28 21:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.089 |  |
| 2026-04-28 21:05:29 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)