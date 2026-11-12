# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_13:15:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 13:15:26 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:15:04 | Urawa (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-11-12 13:14:45 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 13:12:27 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.096 |  |
| 2026-11-12 13:11:39 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-11-12 13:10:10 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.027 |  |
| 2026-11-12 13:10:06 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 13:07:45 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | -0.085 |  |
| 2026-11-12 13:07:05 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | -0.009 |  |
| 2026-11-12 13:07:04 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.069 |  |
| 2026-11-12 13:06:53 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | -0.048 |  |
| 2026-11-12 13:05:30 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-12 13:05:27 | Manampitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-11-12 13:04:37 | Peradeniya (Mahaweli Ganga) | 4.73 | 🟢 Normal | -0.067 |  |
| 2026-11-12 13:04:37 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.098 |  |
| 2026-11-12 13:04:28 | Thaldena (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 13:04:24 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-11-12 13:03:38 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-11-12 13:03:06 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:03:05 | Moraketiya (Walawe Ganga) | 3.84 | 🟡 Alert | -0.010 |  |
| 2026-11-12 13:03:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-12 13:02:54 | Hanwella (Kelani Ganga) | 5.37 | 🟢 Normal | -0.090 |  |
| 2026-11-12 13:02:51 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.061 |  |
| 2026-11-12 13:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.010 |  |
| 2026-11-12 13:02:46 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-11-12 13:02:33 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.135 |  |
| 2026-11-12 13:02:21 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 13:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:02:14 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.041 |  |
| 2026-11-12 13:02:13 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-12 13:02:10 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-11-12 13:01:59 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | -0.097 |  |
| 2026-11-12 13:01:56 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:01:36 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.071 |  |
| 2026-11-12 13:01:14 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.070 |  |
| 2026-11-12 13:01:11 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.022 |  |
| 2026-11-12 13:01:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:00:53 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.147 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 13:10:06 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 13:14:45 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 13:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.010 |  |
| 2026-11-12 13:03:05 | Moraketiya (Walawe Ganga) | 3.84 | 🟡 Alert | -0.010 |  |
| 2026-11-12 13:01:11 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.022 |  |
| 2026-11-12 13:10:10 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.027 |  |
| 2026-11-12 13:01:59 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | -0.097 |  |
| 2026-11-12 13:05:27 | Manampitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-11-12 13:03:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-12 13:02:21 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 13:04:28 | Thaldena (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 13:00:53 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:03:06 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:15:26 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:01:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:05:30 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-12 13:07:05 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | -0.009 |  |
| 2026-11-12 13:01:56 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:11:39 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-11-12 13:02:46 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-11-12 13:02:13 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-12 13:04:24 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-11-12 13:03:38 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-11-12 13:02:14 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.041 |  |
| 2026-11-12 13:06:53 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | -0.048 |  |
| 2026-11-12 13:15:04 | Urawa (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-11-12 13:02:51 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.061 |  |
| 2026-11-12 13:02:10 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-11-12 13:04:37 | Peradeniya (Mahaweli Ganga) | 4.73 | 🟢 Normal | -0.067 |  |
| 2026-11-12 13:07:04 | Badalgama (Maha Oya) | 4.24 | 🟢 Normal | -0.069 |  |
| 2026-11-12 13:01:14 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.070 |  |
| 2026-11-12 13:01:36 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.071 |  |
| 2026-11-12 13:07:45 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | -0.085 |  |
| 2026-11-12 13:02:54 | Hanwella (Kelani Ganga) | 5.37 | 🟢 Normal | -0.090 |  |
| 2026-11-12 13:12:27 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.096 |  |
| 2026-11-12 13:04:37 | Glencourse (Kelani Ganga) | 12.75 | 🟢 Normal | -0.098 |  |
| 2026-11-12 13:02:33 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.135 |  |
| 2026-11-12 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)