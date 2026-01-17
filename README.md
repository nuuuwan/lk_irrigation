# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_12:09:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 12:09:17 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:08:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-17 12:07:13 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:06:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:05:22 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:04:59 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.099 |  |
| 2026-01-17 12:04:56 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:04:51 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:04:48 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-17 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-17 12:04:14 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:04:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:04:01 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.230 |  |
| 2026-01-17 12:03:58 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:42 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:03:40 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.023 |  |
| 2026-01-17 12:03:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:21 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:11 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-17 12:03:04 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:02 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.013 |  |
| 2026-01-17 12:02:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-17 12:02:29 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:29 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:12 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:43 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:37 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-17 12:01:33 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:08 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.208 |  |
| 2026-01-17 12:01:06 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-17 11:59:07 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 12:01:37 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-17 12:03:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-17 12:08:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-17 12:04:48 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-17 12:04:30 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-17 12:01:06 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-17 12:01:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:58 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:11 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 11:59:07 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:05:22 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:12 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:04 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:43 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:04:14 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:07:13 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:29 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:09:17 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:06:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:21 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:01:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:29 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:04:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 12:03:42 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:04:51 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:04:56 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-17 12:03:02 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.013 |  |
| 2026-01-17 12:02:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-17 12:03:40 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.023 |  |
| 2026-01-17 12:04:59 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.099 |  |
| 2026-01-17 12:01:08 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.208 |  |
| 2026-01-17 12:04:01 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)