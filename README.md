# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_03:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 03:18:27 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-15 03:15:07 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:14:24 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.537 |  |
| 2026-01-15 03:13:17 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.537 |  |
| 2026-01-15 03:12:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:12:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 03:11:11 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:09:56 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.088 |  |
| 2026-01-15 03:09:15 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-01-15 03:08:02 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-15 03:07:42 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-15 03:07:38 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-15 03:06:08 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:06:04 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.003 |  |
| 2026-01-15 03:05:50 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 03:04:54 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.035 |  |
| 2026-01-15 03:04:46 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-15 03:04:43 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:04:42 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:04:00 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-15 03:03:40 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:03:17 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:02:46 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:02:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-15 03:02:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-01-15 03:02:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:02:10 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:01:50 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:01:24 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:01:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:00:55 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-01-15 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:00:07 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.025 |  |
| 2026-01-15 02:59:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:49:12 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:21:47 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.081 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 02:08:51 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-01-15 03:08:02 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-01-15 03:04:46 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-15 02:21:47 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-15 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 01:39:57 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-15 03:02:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-15 03:12:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 03:18:27 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-15 03:02:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:01:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:03:17 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:04:43 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:11:11 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 02:02:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:02:46 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:12:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:15:07 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:05:50 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:01:24 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 03:06:04 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.003 |  |
| 2026-01-15 00:02:34 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:03:40 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:01:50 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:02:10 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-15 03:04:00 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-01-15 03:09:15 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 02:01:15 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 03:00:07 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.025 |  |
| 2026-01-15 03:00:55 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-01-15 03:02:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-01-15 01:01:14 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.034 |  |
| 2026-01-15 03:04:54 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.035 |  |
| 2026-01-15 03:09:56 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.088 |  |
| 2026-01-15 03:14:24 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.537 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)