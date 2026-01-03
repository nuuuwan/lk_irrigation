# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_08:01:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,299 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 08:01:50 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:16 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:01:15 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:00:51 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:39:02 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:24:07 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2026-01-03 07:16:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-01-03 07:11:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-01-03 07:10:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-03 07:10:05 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:09:43 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:08:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-03 07:08:13 | Galgamuwa (Mee Oya) | 1.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 07:07:32 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.038 |  |
| 2026-01-03 07:06:58 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-03 07:06:45 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:41 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:05:12 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:56 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:04:20 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-01-03 07:04:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:03 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 07:10:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-03 07:08:13 | Galgamuwa (Mee Oya) | 1.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-03 07:03:36 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:02:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 07:09:43 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 08:01:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:00:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:58 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:36 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:45 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:10:05 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:00:26 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:01:39 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:02:38 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:10:20 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 08:01:15 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:06:41 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 07:05:12 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-01-03 08:01:50 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:03:37 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:01:30 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:04:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 07:24:07 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.015 |  |
| 2026-01-03 07:16:20 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-01-03 08:00:51 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.020 |  |
| 2026-01-03 07:03:58 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-03 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-03 08:01:16 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-01-03 07:11:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-01-03 07:03:00 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-01-03 07:07:32 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.038 |  |
| 2026-01-03 07:04:20 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.041 |  |
| 2026-01-03 07:01:33 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.044 |  |
| 2026-01-03 07:08:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-01-03 07:06:53 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-01-03 07:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.137 |  |
| 2026-01-03 07:04:01 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.290 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)