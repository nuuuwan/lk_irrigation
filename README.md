# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_10:13:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,592 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 10:13:41 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.091 |  |
| 2026-08-04 10:13:15 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-08-04 10:09:40 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:09:33 | Rathnapura (Kalu Ganga) | 6.99 | 🟡 Alert | -0.123 |  |
| 2026-08-04 10:09:17 | Nagalagam Street (Kelani Ganga) | 1.08 | 🟢 Normal | -0.056 |  |
| 2026-08-04 10:08:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:07:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:07:11 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.038 |  |
| 2026-08-04 10:06:28 | Glencourse (Kelani Ganga) | 14.06 | 🟢 Normal | -0.242 |  |
| 2026-08-04 10:06:03 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-04 10:05:59 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.112 |  |
| 2026-08-04 10:05:03 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:53 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-08-04 10:04:43 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:04 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:02 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:03:49 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:03:48 | Hanwella (Kelani Ganga) | 6.61 | 🟢 Normal | -0.119 |  |
| 2026-08-04 10:03:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:03:28 | Nawalapitiya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-08-04 10:03:17 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.178 |  |
| 2026-08-04 10:03:11 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 10:03:05 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.099 |  |
| 2026-08-04 10:02:49 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.000 |  |
| 2026-08-04 10:02:33 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-04 10:02:33 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:25 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 10:02:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:23 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:06 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:01:14 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-04 10:01:08 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-08-04 10:00:56 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.085 |  |
| 2026-08-04 10:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:00:48 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:00:46 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.061 |  |
| 2026-08-04 09:39:56 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.106 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 10:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.000 |  |
| 2026-08-04 10:09:33 | Rathnapura (Kalu Ganga) | 6.99 | 🟡 Alert | -0.123 |  |
| 2026-08-04 10:03:28 | Nawalapitiya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-08-04 10:02:33 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-04 10:06:03 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-04 10:01:14 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-04 10:03:11 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 10:02:25 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 10:02:49 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:02 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:33 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:07:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:24 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:06 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:03:49 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:08:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:43 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:02:23 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:04:04 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:05:03 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:09:40 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:00:48 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 09:01:48 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:03:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-04 10:13:15 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-08-04 10:01:08 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-08-04 10:04:53 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-08-04 10:07:11 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.038 |  |
| 2026-08-04 10:09:17 | Nagalagam Street (Kelani Ganga) | 1.08 | 🟢 Normal | -0.056 |  |
| 2026-08-04 10:00:46 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.061 |  |
| 2026-08-04 10:00:56 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.085 |  |
| 2026-08-04 10:13:41 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.091 |  |
| 2026-08-04 10:03:05 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.099 |  |
| 2026-08-04 10:05:59 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.112 |  |
| 2026-08-04 10:03:48 | Hanwella (Kelani Ganga) | 6.61 | 🟢 Normal | -0.119 |  |
| 2026-08-04 10:03:17 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.178 |  |
| 2026-08-04 10:06:28 | Glencourse (Kelani Ganga) | 14.06 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)