# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_14:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 14:13:50 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-10-07 14:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.042 |  |
| 2026-10-07 14:11:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.081 |  |
| 2026-10-07 14:10:40 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:09:44 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-10-07 14:08:50 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:08:39 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:08:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.058 |  |
| 2026-10-07 14:07:41 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-10-07 14:07:34 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.095 |  |
| 2026-10-07 14:07:14 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:05:59 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:05:41 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-10-07 14:05:11 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-07 14:04:50 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-10-07 14:04:40 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.030 |  |
| 2026-10-07 14:04:37 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:04:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:04:18 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 14:04:11 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:03:46 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-07 14:03:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-07 14:02:54 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:02:48 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:02:48 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.088 |  |
| 2026-10-07 14:02:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.117 |  |
| 2026-10-07 14:02:37 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:02:27 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:02:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.078 |  |
| 2026-10-07 14:02:14 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-10-07 14:02:14 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-10-07 14:02:07 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:01:57 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.050 |  |
| 2026-10-07 14:01:46 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-07 14:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:01:32 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 14:01:11 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-10-07 14:01:07 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 14:02:48 | Panadugama (Nilwala Ganga) | 5.14 | 🟡 Alert | -0.088 |  |
| 2026-10-07 14:03:46 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-07 14:04:18 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 14:01:07 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:02:37 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:08:39 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:10:40 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:04:11 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:07:14 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:08:50 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:04:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:02:07 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:04:37 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:00:44 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:02:48 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 14:13:50 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-10-07 14:05:11 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-10-07 14:01:32 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 14:01:11 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-10-07 14:05:41 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-10-07 14:03:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-07 14:02:54 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:02:27 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:05:59 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-07 14:01:46 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-07 14:07:41 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-10-07 14:04:40 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.030 |  |
| 2026-10-07 14:09:44 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-10-07 14:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.042 |  |
| 2026-10-07 14:02:14 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-10-07 14:01:57 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.050 |  |
| 2026-10-07 14:04:50 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-10-07 14:08:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.058 |  |
| 2026-10-07 14:02:14 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-10-07 14:02:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.078 |  |
| 2026-10-07 14:11:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.081 |  |
| 2026-10-07 14:07:34 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.095 |  |
| 2026-10-07 14:02:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)