# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_17:27:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,403 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 17:27:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:12:16 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-11-08 17:09:41 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 17:08:30 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-08 17:08:10 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 17:07:56 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.080 |  |
| 2026-11-08 17:07:39 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.058 |  |
| 2026-11-08 17:06:54 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | -0.049 |  |
| 2026-11-08 17:06:41 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:06:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.177 |  |
| 2026-11-08 17:06:14 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-11-08 17:05:19 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.048 |  |
| 2026-11-08 17:05:17 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:04:52 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:04:50 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-11-08 17:04:41 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-08 17:04:38 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-08 17:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.43 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 17:04:04 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-08 17:03:53 | Magura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.168 |  |
| 2026-11-08 17:03:43 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-11-08 17:03:41 | Holombuwa (Kelani Ganga) | 2.05 | 🟢 Normal | 0.860 | 🔺 Rising |
| 2026-11-08 17:03:31 | Moraketiya (Walawe Ganga) | 3.12 | 🟡 Alert | -0.029 |  |
| 2026-11-08 17:03:11 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 17:03:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-08 17:02:38 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:02:32 | Moragaswewa (Deduru Oya) | 3.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-08 17:02:17 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.040 |  |
| 2026-11-08 17:02:05 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-08 17:02:00 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-08 17:01:52 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:01:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-08 17:01:48 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-11-08 17:01:47 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-08 17:01:39 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 17:01:31 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-11-08 17:01:14 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.070 |  |
| 2026-11-08 17:00:27 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:59:17 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 17:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.43 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 17:09:41 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 17:12:16 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-11-08 17:03:31 | Moraketiya (Walawe Ganga) | 3.12 | 🟡 Alert | -0.029 |  |
| 2026-11-08 17:07:56 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.080 |  |
| 2026-11-08 17:03:41 | Holombuwa (Kelani Ganga) | 2.05 | 🟢 Normal | 0.860 | 🔺 Rising |
| 2026-11-08 17:01:31 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.669 | 🔺 Rising |
| 2026-11-08 17:01:47 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-08 17:04:50 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-11-08 17:04:41 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-08 17:01:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-11-08 17:04:38 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-08 17:02:00 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-08 17:02:05 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-08 17:08:30 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-08 17:08:10 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 17:01:39 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 17:04:04 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-08 17:03:11 | Putupaula (Kalu Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 17:02:32 | Moragaswewa (Deduru Oya) | 3.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-08 17:27:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:05:17 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:01:52 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:06:41 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:07:50 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:04:52 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:02:38 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:00:27 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-08 17:03:02 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-08 17:03:43 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-11-08 17:01:48 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-11-08 17:02:17 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.040 |  |
| 2026-11-08 17:05:19 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.048 |  |
| 2026-11-08 17:06:14 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-11-08 17:06:54 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | -0.049 |  |
| 2026-11-08 17:07:39 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.058 |  |
| 2026-11-08 17:01:14 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.070 |  |
| 2026-11-08 17:03:53 | Magura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.168 |  |
| 2026-11-08 17:06:22 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)