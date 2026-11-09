# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_19:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Nawalapitiya — Alert; 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 19:03:19 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.072 |  |
| 2026-11-09 19:02:47 | Deraniyagala (Kelani Ganga) | 3.43 | 🟢 Normal | -0.204 |  |
| 2026-11-09 19:02:22 | Glencourse (Kelani Ganga) | 12.53 | 🟢 Normal | 1.470 | 🔺 Rising |
| 2026-11-09 19:02:20 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:02:18 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.020 |  |
| 2026-11-09 19:02:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-09 19:01:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-11-09 19:01:43 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 19:01:34 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-11-09 19:01:19 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:01:13 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-09 19:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 18:04:27 | Nawalapitiya (Mahaweli Ganga) | 3.68 | 🟡 Alert | 1.462 | 🔺 Rising |
| 2026-11-09 18:00:32 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 18:13:27 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-11-09 18:02:56 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 17:58:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 18:01:46 | Magura (Kalu Ganga) | 4.45 | 🟡 Alert | -0.023 |  |
| 2026-11-09 18:05:49 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | -0.045 |  |
| 2026-11-09 19:02:22 | Glencourse (Kelani Ganga) | 12.53 | 🟢 Normal | 1.470 | 🔺 Rising |
| 2026-11-09 18:05:25 | Wellawaya (Kirindi Oya) | 3.16 | 🟢 Normal | 1.191 | 🔺 Rising |
| 2026-11-09 18:02:17 | Peradeniya (Mahaweli Ganga) | 4.64 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-11-09 18:08:09 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-11-09 18:05:51 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-11-09 18:03:15 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-11-09 18:04:48 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 18:02:40 | Thaldena (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-11-09 18:02:55 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-09 18:03:46 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-09 19:00:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 19:01:43 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 18:02:25 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:00:21 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:02:20 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:01:19 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:05:33 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:02:19 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:02:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-09 19:01:13 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-11-09 19:02:18 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.020 |  |
| 2026-11-09 18:00:18 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-11-09 19:01:34 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-11-09 18:07:49 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.036 |  |
| 2026-11-09 19:01:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-11-09 19:03:19 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.072 |  |
| 2026-11-09 19:02:47 | Deraniyagala (Kelani Ganga) | 3.43 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)