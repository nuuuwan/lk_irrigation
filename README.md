# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_21:15:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 21:15:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.282 |  |
| 2026-11-27 21:14:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-27 21:13:17 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-27 21:13:16 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:10:01 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-27 21:09:49 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 21:09:29 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.130 |  |
| 2026-11-27 21:09:25 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-27 21:06:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-11-27 21:06:07 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.082 |  |
| 2026-11-27 21:06:02 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:05:55 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-27 21:05:16 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.160 |  |
| 2026-11-27 21:05:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:05:12 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:05:10 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 21:04:43 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 21:04:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.173 |  |
| 2026-11-27 21:04:21 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | -0.041 |  |
| 2026-11-27 21:04:09 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-11-27 21:03:54 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:03:51 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:03:23 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-27 21:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.021 |  |
| 2026-11-27 21:03:11 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-27 21:03:01 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 21:03:00 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:02:55 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 21:02:55 | Dunamale (Aththanagalu Oya) | 3.49 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 21:02:46 | Moraketiya (Walawe Ganga) | 3.71 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-11-27 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-27 21:02:23 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-11-27 21:02:10 | Kuda Oya (Kirindi Oya) | 3.55 | 🟢 Normal | 1.071 | 🔺 Rising |
| 2026-11-27 21:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:01:55 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.209 |  |
| 2026-11-27 21:00:13 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 21:00:10 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 21:02:46 | Moraketiya (Walawe Ganga) | 3.71 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-11-27 21:02:55 | Dunamale (Aththanagalu Oya) | 3.49 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 21:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.021 |  |
| 2026-11-27 21:02:10 | Kuda Oya (Kirindi Oya) | 3.55 | 🟢 Normal | 1.071 | 🔺 Rising |
| 2026-11-27 21:03:11 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-27 21:05:55 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-27 21:09:25 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-27 21:03:23 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-27 21:02:55 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 21:00:13 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 21:05:10 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 21:03:01 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 21:10:01 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-27 21:09:49 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 21:13:17 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-27 21:04:43 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 21:14:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-27 21:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:05:12 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:13:16 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:05:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:03:54 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:03:00 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:03:51 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:00:10 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:04:09 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-11-27 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 21:02:23 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-11-27 21:04:21 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | -0.041 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-27 21:06:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-11-27 21:06:07 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.082 |  |
| 2026-11-27 21:09:29 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.130 |  |
| 2026-11-27 21:05:16 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | -0.160 |  |
| 2026-11-27 21:04:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.173 |  |
| 2026-11-27 21:01:55 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.209 |  |
| 2026-11-27 21:15:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.282 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)