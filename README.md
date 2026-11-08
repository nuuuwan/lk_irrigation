# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_20:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 20:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-08 20:02:47 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-08 20:02:43 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:02:42 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:02:11 | Holombuwa (Kelani Ganga) | 3.79 | 🟠 Minor Flood | -0.109 |  |
| 2026-11-08 20:01:41 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:01:30 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 20:00:14 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-11-08 20:00:01 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-11-08 19:29:47 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-08 19:23:02 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 20:02:11 | Holombuwa (Kelani Ganga) | 3.79 | 🟠 Minor Flood | -0.109 |  |
| 2026-11-08 20:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-08 19:06:14 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-11-08 20:00:14 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | 0.000 |  |
| 2026-11-08 19:05:54 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 19:09:13 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.028 |  |
| 2026-11-08 19:04:19 | Glencourse (Kelani Ganga) | 12.37 | 🟢 Normal | 0.925 | 🔺 Rising |
| 2026-11-08 20:00:01 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-11-08 19:01:16 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-11-08 20:02:47 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-08 20:02:42 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-11-08 19:05:02 | Deraniyagala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-11-08 19:03:38 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-11-08 19:07:14 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-08 19:02:21 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-08 19:16:06 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-08 19:07:57 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 19:00:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 19:01:00 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 20:01:30 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 19:13:46 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-08 19:23:02 | Moragaswewa (Deduru Oya) | 3.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-08 19:08:59 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | 0.005 |  |
| 2026-11-08 19:08:59 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:15 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:05:13 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:23 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 20:02:43 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:19:37 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.008 |  |
| 2026-11-08 19:07:48 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 20:01:41 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-08 20:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-08 19:07:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-11-08 19:03:42 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.032 |  |
| 2026-11-08 19:09:38 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.038 |  |
| 2026-11-08 19:01:02 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)