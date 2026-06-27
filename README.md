# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_15:24:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 15:24:35 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:11:22 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 15:09:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:08:46 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:08:42 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-27 15:08:27 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 15:07:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-06-27 15:06:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:06:47 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:06:37 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:06:13 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.013 |  |
| 2026-06-27 15:05:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:05:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:54 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:25 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:06 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:02 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:03:55 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:03:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:03:14 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-27 15:03:13 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.023 |  |
| 2026-06-27 15:03:02 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:03:01 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-27 15:02:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:33 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-27 15:02:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:19 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.012 |  |
| 2026-06-27 15:02:14 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2026-06-27 15:02:10 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:03 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.013 |  |
| 2026-06-27 15:01:55 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-06-27 15:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-06-27 15:01:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 15:01:15 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:01:14 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:01:08 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:00:14 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 15:03:14 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-27 15:08:42 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-27 15:11:22 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 15:08:27 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 15:01:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 15:02:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:25 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:06:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:03:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:02 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:08:46 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:00:14 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:01:14 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:05:46 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:54 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:24:35 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:06:37 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:02:10 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:06:47 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:02:19 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:01:08 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:03:02 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:01:15 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:03:55 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-06-27 14:02:02 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-27 15:03:01 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-06-27 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.012 |  |
| 2026-06-27 15:02:03 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.013 |  |
| 2026-06-27 15:06:13 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.013 |  |
| 2026-06-27 15:01:55 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-06-27 15:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-06-27 15:03:13 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.023 |  |
| 2026-06-27 15:02:14 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2026-06-27 15:02:33 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-27 15:07:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)