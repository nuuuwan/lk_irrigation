# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_07:22:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 07:22:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:19:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:17:53 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-28 07:16:23 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2026-01-28 07:12:23 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:10:34 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-01-28 07:10:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-28 07:09:25 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:08:27 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-28 07:06:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.075 |  |
| 2026-01-28 07:06:34 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-28 07:05:59 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:44 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-28 07:05:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:05 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:22 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.173 |  |
| 2026-01-28 07:04:02 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.085 |  |
| 2026-01-28 07:03:59 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.093 |  |
| 2026-01-28 07:03:40 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:03:20 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:03:18 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:03:10 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-28 07:02:57 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:02:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-01-28 07:02:39 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.053 |  |
| 2026-01-28 07:02:37 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-28 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.062 |  |
| 2026-01-28 07:02:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:02:12 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:01:57 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.089 |  |
| 2026-01-28 07:01:37 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:00:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.024 |  |
| 2026-01-28 07:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 06:33:37 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-28 06:28:02 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 07:06:34 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-28 07:03:10 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-28 07:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-28 07:10:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-28 07:17:53 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-28 07:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 06:03:33 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:09:25 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:44 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:03:20 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:19:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:03:18 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:12:23 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:22 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:04:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:02:57 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:02:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:59 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:22:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:01:37 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:05:05 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 07:16:23 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2026-01-28 07:02:37 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:03:40 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:02:12 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-28 07:02:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-01-28 07:08:27 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-01-28 07:00:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.024 |  |
| 2026-01-28 07:10:34 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-01-28 07:05:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-01-28 07:02:39 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.053 |  |
| 2026-01-28 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.062 |  |
| 2026-01-28 07:06:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.075 |  |
| 2026-01-28 07:04:02 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.085 |  |
| 2026-01-28 07:01:57 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.089 |  |
| 2026-01-28 07:03:59 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.093 |  |
| 2026-01-28 07:04:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)