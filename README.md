# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_14:20:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 14:20:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:20:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.041 |  |
| 2026-01-26 14:14:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:09:39 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-26 14:08:34 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:07:37 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:07:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:06:30 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:06:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:06:13 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 14:05:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.066 |  |
| 2026-01-26 14:05:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.041 |  |
| 2026-01-26 14:05:19 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-26 14:04:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:04:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 14:04:29 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-01-26 14:04:06 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.019 |  |
| 2026-01-26 14:04:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-26 14:04:00 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-26 14:03:50 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:31 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:03:25 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:12 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 14:02:58 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 14:02:29 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.079 |  |
| 2026-01-26 14:02:11 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:58 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:01:53 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-01-26 14:01:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-26 14:01:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:11 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 14:01:09 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:00:38 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-26 14:00:14 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 14:04:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-26 14:05:19 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-26 14:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-26 14:01:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-26 14:01:11 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 14:06:13 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 14:02:58 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 14:04:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 14:03:12 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 14:01:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:02:11 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 13:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:58 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:06:30 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:08:34 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:07:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:07:37 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:25 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:14:04 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:09 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:09:39 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:20:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:01:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:03:50 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 14:04:00 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-26 14:00:38 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-26 14:00:14 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-26 14:01:53 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.012 |  |
| 2026-01-26 14:04:06 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.019 |  |
| 2026-01-26 14:06:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:03:31 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:01:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-01-26 14:04:29 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-01-26 14:05:23 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.041 |  |
| 2026-01-26 14:20:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.041 |  |
| 2026-01-26 14:05:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.066 |  |
| 2026-01-26 14:02:29 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)