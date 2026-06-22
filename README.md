# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_15:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,381 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 15:18:13 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:17:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:12:49 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-06-22 15:07:23 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.045 |  |
| 2026-06-22 15:07:17 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-22 15:07:17 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:07:10 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-22 15:05:51 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 15:05:46 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:05:45 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:05:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 15:05:18 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.117 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 15:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-06-22 14:06:28 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-22 15:12:49 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-06-22 15:05:18 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-22 15:02:56 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-22 15:03:36 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-22 15:07:17 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-22 15:03:25 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-22 15:07:10 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-22 15:04:27 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-22 15:02:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-22 15:05:31 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 15:05:51 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 15:03:18 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-22 15:00:21 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:02:03 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:03:28 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:01:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:00:42 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:04:52 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 14:04:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:18:13 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:00:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:03:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:00:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:03:50 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:05:45 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:05:46 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:03:49 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:07:17 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:03:44 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 15:00:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-22 15:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-22 15:01:09 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-06-22 15:00:46 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.040 |  |
| 2026-06-22 15:07:23 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.045 |  |
| 2026-06-22 15:03:09 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.059 |  |
| 2026-06-22 15:02:14 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)