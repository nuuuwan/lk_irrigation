# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_16:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 16:13:16 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:11:22 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-24 16:10:16 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-24 16:07:51 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-24 16:07:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-24 16:07:34 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:06:58 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-24 16:06:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:05:55 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:05:32 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:04:34 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:04:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 16:04:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:03:47 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:03:32 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-24 16:03:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-01-24 16:03:16 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-24 16:03:12 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:02:58 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:02:43 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:02:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:02:34 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.051 |  |
| 2026-01-24 16:02:28 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 16:02:19 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.012 |  |
| 2026-01-24 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:01:52 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-24 16:01:48 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:01:31 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:01:24 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:01:23 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:01:23 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:01:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-24 16:01:11 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:00:56 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:00:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 16:10:16 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-24 16:03:32 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-24 16:01:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-24 16:07:51 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-24 16:03:16 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-24 16:11:22 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-24 16:07:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-24 16:02:28 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 16:04:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 16:06:58 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-24 16:01:48 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:00:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:04:34 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:13:16 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:34 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 15:02:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:02:58 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 15:06:37 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:03:12 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:03:47 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:05:32 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:06:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:05:55 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:01:23 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:04:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:02:43 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:01:24 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:00:56 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:02:19 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | -0.012 |  |
| 2026-01-24 16:01:31 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:02:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:01:23 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:03:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-01-24 16:01:52 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-24 15:02:22 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-01-24 16:02:34 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)