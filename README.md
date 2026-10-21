# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_02:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 02:08:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:08:31 | Glencourse (Kelani Ganga) | 13.43 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-22 02:07:05 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | -0.287 |  |
| 2026-10-22 02:06:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 02:05:46 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-22 02:05:17 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-22 02:04:59 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-10-22 02:04:43 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-10-22 02:04:21 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:04:06 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.239 |  |
| 2026-10-22 02:03:56 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-22 02:03:43 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-22 02:03:32 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.325 |  |
| 2026-10-22 02:03:21 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 02:03:21 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 02:02:58 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | 0.466 | 🔺 Rising |
| 2026-10-22 02:02:48 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 02:02:38 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-22 02:02:14 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 02:02:01 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-10-22 02:01:46 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-10-22 02:01:40 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-22 02:01:26 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-10-22 02:01:23 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 02:01:46 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-10-22 00:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 01:05:15 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-10-22 02:02:58 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | 0.466 | 🔺 Rising |
| 2026-10-22 02:05:17 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-22 02:04:59 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-10-22 02:08:31 | Glencourse (Kelani Ganga) | 13.43 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-22 02:03:56 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 01:01:42 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-22 00:05:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 02:01:40 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-22 02:03:21 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-22 02:03:43 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-21 23:04:34 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 01:02:56 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 00:04:14 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 02:03:21 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 02:02:48 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 01:00:13 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 02:02:14 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 02:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 02:06:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 02:05:46 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-22 02:02:01 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-10-22 02:04:43 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-10-22 02:02:38 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-22 02:08:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:04:21 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:01:23 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:01:26 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-10-22 01:05:37 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.052 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 01:02:41 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.120 |  |
| 2026-10-22 02:04:06 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.239 |  |
| 2026-10-22 02:07:05 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | -0.287 |  |
| 2026-10-22 02:03:32 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.325 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)