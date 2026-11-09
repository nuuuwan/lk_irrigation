# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_20:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Norwood — Alert; 🟡 Dunamale — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 20:03:50 | Norwood (Kelani Ganga) | 1.70 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 20:03:26 | Deraniyagala (Kelani Ganga) | 3.18 | 🟢 Normal | -0.247 |  |
| 2026-11-09 20:02:53 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 20:02:45 | Nawalapitiya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.238 |  |
| 2026-11-09 20:02:29 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-09 20:02:19 | Wellawaya (Kirindi Oya) | 2.98 | 🟢 Normal | -0.722 |  |
| 2026-11-09 20:02:11 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-09 20:02:01 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-09 20:01:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-09 20:01:53 | Nakkala (Kumbukkan Oya) | 1.86 | 🟢 Normal | 0.738 | 🔺 Rising |
| 2026-11-09 20:00:48 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-09 20:00:38 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-09 20:00:14 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:14:33 | Baddegama (Gin Ganga) | 3.64 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 19:14:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:13:04 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.027 |  |
| 2026-11-09 19:12:23 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 19:03:55 | Kithulgala (Kelani Ganga) | 3.50 | 🟡 Alert | 1.230 | 🔺 Rising |
| 2026-11-09 19:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-11-09 19:14:33 | Baddegama (Gin Ganga) | 3.64 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 20:03:50 | Norwood (Kelani Ganga) | 1.70 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 19:03:42 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | 0.000 |  |
| 2026-11-09 20:02:53 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-09 19:11:04 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | -0.017 |  |
| 2026-11-09 19:13:04 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.027 |  |
| 2026-11-09 19:02:22 | Glencourse (Kelani Ganga) | 12.53 | 🟢 Normal | 1.470 | 🔺 Rising |
| 2026-11-09 19:08:55 | Thaldena (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.869 | 🔺 Rising |
| 2026-11-09 20:02:29 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-09 20:01:53 | Nakkala (Kumbukkan Oya) | 1.86 | 🟢 Normal | 0.738 | 🔺 Rising |
| 2026-11-09 19:08:31 | Thawalama (Gin Ganga) | 3.83 | 🟢 Normal | 0.676 | 🔺 Rising |
| 2026-11-09 19:03:37 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-09 20:02:01 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-09 19:04:50 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-09 20:00:48 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-09 20:02:11 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-09 19:07:01 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-09 19:11:05 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-09 19:12:23 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:14:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:05:06 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 20:00:38 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-09 20:00:14 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 19:05:38 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-11-09 19:04:11 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-09 19:02:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-09 19:02:18 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.020 |  |
| 2026-11-09 20:01:57 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-09 19:01:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-11-09 19:03:19 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.072 |  |
| 2026-11-09 20:02:45 | Nawalapitiya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.238 |  |
| 2026-11-09 20:03:26 | Deraniyagala (Kelani Ganga) | 3.18 | 🟢 Normal | -0.247 |  |
| 2026-11-09 20:02:19 | Wellawaya (Kirindi Oya) | 2.98 | 🟢 Normal | -0.722 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)