# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_21:26:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 21:26:11 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:17:30 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-22 21:17:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.46 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-22 21:17:01 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 21:13:32 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 21:12:20 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-06-22 21:09:59 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-22 21:09:52 | Glencourse (Kelani Ganga) | 12.01 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-06-22 21:08:39 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-22 21:06:26 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 21:06:24 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 21:06:17 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:06:12 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-06-22 21:05:49 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 21:05:42 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-22 21:05:31 | Holombuwa (Kelani Ganga) | 1.88 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-06-22 21:05:12 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:04:45 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-22 21:04:45 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:04:19 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-06-22 21:04:12 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-22 21:04:08 | Deraniyagala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-06-22 21:03:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 21:03:44 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:03:40 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |
| 2026-06-22 21:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:20 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:12 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-06-22 21:02:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:10 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-22 21:02:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:00:37 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-06-22 21:00:20 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:00:11 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 21:17:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.46 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-22 21:05:31 | Holombuwa (Kelani Ganga) | 1.88 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-06-22 21:09:52 | Glencourse (Kelani Ganga) | 12.01 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-06-22 21:04:08 | Deraniyagala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-06-22 21:12:20 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-06-22 21:05:42 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-22 21:00:37 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-06-22 21:02:12 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-06-22 21:02:10 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-22 21:04:45 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-22 21:04:12 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-22 21:08:39 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-22 21:09:59 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-22 21:05:49 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 21:17:30 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-22 21:13:32 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 21:17:01 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 20:07:09 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 21:06:24 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 21:03:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 21:06:26 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 21:00:11 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:20 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:26:11 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:05:12 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:00:20 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:04:45 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:03:44 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 21:02:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-22 21:04:19 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-06-22 21:06:12 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-06-22 21:03:40 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)