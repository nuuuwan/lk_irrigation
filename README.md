# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_23:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 23:10:20 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-22 23:09:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:09:25 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-22 23:07:41 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 23:06:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 23:06:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.057 |  |
| 2026-06-22 23:06:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:04:38 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-22 23:04:28 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-06-22 23:04:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:03:55 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-22 23:03:42 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-06-22 23:03:41 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-22 23:03:12 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-22 23:03:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-22 23:02:54 | Deraniyagala (Kelani Ganga) | 2.61 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-22 23:02:39 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:32 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.234 | 🔺 Rising |
| 2026-06-22 23:02:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:21 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 2.102 | 🔺 Rising |
| 2026-06-22 23:02:19 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 23:02:08 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:08 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-06-22 23:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-22 23:01:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:32 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-22 23:01:26 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-06-22 23:01:18 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-22 23:01:14 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:00:54 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-22 22:33:48 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 2.102 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 23:02:32 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.234 | 🔺 Rising |
| 2026-06-22 22:18:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-06-22 23:02:21 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 2.102 | 🔺 Rising |
| 2026-06-22 23:03:42 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | 0.402 | 🔺 Rising |
| 2026-06-22 23:02:54 | Deraniyagala (Kelani Ganga) | 2.61 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-22 23:01:26 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-06-22 23:04:28 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-06-22 23:02:08 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-06-22 23:03:12 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-22 23:03:41 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-22 23:10:20 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-22 23:03:55 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-22 23:09:25 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-22 23:04:38 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-22 23:02:19 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 23:06:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 23:01:18 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-22 22:22:57 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-22 22:01:58 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 23:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-22 23:07:41 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 23:03:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:00:54 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-22 22:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:06:02 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:36 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:39 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:09:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:04:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:14 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:02:08 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 23:01:32 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-22 23:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-22 23:06:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)