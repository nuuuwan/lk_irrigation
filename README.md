# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_22:24:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,590 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 22:24:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-08 22:19:09 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 22:18:03 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:17:24 | Magura (Kalu Ganga) | 4.53 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-11-08 22:15:23 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-11-08 22:12:23 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:12:22 | Putupaula (Kalu Ganga) | 2.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 22:11:18 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 22:09:24 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 22:09:18 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-11-08 22:08:59 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.204 |  |
| 2026-11-08 22:08:58 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:08:50 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.027 |  |
| 2026-11-08 22:08:41 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:08:24 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:07:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-08 22:06:26 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:05:36 | Holombuwa (Kelani Ganga) | 2.92 | 🟢 Normal | -0.432 |  |
| 2026-11-08 22:04:51 | Glencourse (Kelani Ganga) | 13.45 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-11-08 22:03:46 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.095 |  |
| 2026-11-08 22:03:30 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 22:03:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:03:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-08 22:02:29 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-11-08 22:02:22 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:02:22 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.173 |  |
| 2026-11-08 22:02:21 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.061 |  |
| 2026-11-08 22:02:07 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:01:38 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:01:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-11-08 22:01:37 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 22:01:23 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:01:06 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 22:01:00 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-08 22:00:56 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | 0.000 |  |
| 2026-11-08 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 22:02:29 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-11-08 22:17:24 | Magura (Kalu Ganga) | 4.53 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-11-08 22:15:23 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-11-08 22:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-08 22:19:09 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 22:00:56 | Moraketiya (Walawe Ganga) | 3.08 | 🟡 Alert | 0.000 |  |
| 2026-11-08 22:02:21 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.061 |  |
| 2026-11-08 22:09:18 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-11-08 22:04:51 | Glencourse (Kelani Ganga) | 13.45 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-11-08 22:01:00 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-08 22:03:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-08 22:07:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-08 22:24:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-08 22:12:22 | Putupaula (Kalu Ganga) | 2.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 22:11:18 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 22:01:06 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 22:09:24 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 22:01:23 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:02:22 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 22:01:37 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:18:03 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:12:23 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:08:58 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:08:24 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:03:30 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:01:38 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:08:41 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:03:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:02:07 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:01:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-11-08 22:08:50 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.027 |  |
| 2026-11-08 22:03:46 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.095 |  |
| 2026-11-08 22:02:22 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.173 |  |
| 2026-11-08 22:08:59 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.204 |  |
| 2026-11-08 22:05:36 | Holombuwa (Kelani Ganga) | 2.92 | 🟢 Normal | -0.432 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)