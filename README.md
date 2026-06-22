# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_01:25:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,753 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 01:25:21 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 01:19:29 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-06-23 01:17:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-06-23 01:16:58 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 01:15:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:11:38 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-23 01:10:14 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-23 01:09:16 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | -0.171 |  |
| 2026-06-23 01:06:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:06:25 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-23 01:05:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:05:14 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-23 01:04:24 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:04:21 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-23 01:04:16 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-23 01:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 01:03:51 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.139 |  |
| 2026-06-23 01:03:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:59 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:28 | Deraniyagala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.293 |  |
| 2026-06-23 01:02:28 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-06-23 01:02:25 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-23 01:02:07 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-23 01:02:01 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:47 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-06-23 01:01:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.021 |  |
| 2026-06-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:42 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:41 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 01:01:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:00:24 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 01:01:47 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-06-23 01:17:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-06-23 01:05:14 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-23 01:19:29 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-06-23 01:04:16 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-23 01:04:21 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-23 01:06:25 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-23 01:02:07 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-23 00:02:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-23 01:25:21 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 01:10:14 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-23 01:16:58 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 01:11:38 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-23 01:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 00:06:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 01:01:41 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:08:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 00:01:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:42 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:01 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:03:58 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:05:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:03:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:15:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:04:24 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:06:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:59 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:00:24 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 00:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:02:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-23 01:02:28 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-06-23 01:01:46 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.021 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 01:03:51 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.139 |  |
| 2026-06-23 01:09:16 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | -0.171 |  |
| 2026-06-23 01:02:28 | Deraniyagala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.293 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)