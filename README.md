# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_15:29:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Peradeniya — Minor Flood; 🟡 Glencourse — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Thawalama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 15:29:29 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 15:09:06 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-20 15:07:12 | Thawalama (Gin Ganga) | 5.14 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-09-20 15:07:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-20 15:06:55 | Holombuwa (Kelani Ganga) | 3.10 | 🟡 Alert | -0.151 |  |
| 2026-09-20 15:06:01 | Rathnapura (Kalu Ganga) | 6.86 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-20 15:05:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:05:41 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:05:35 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:04:41 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 15:04:41 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:04:08 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-20 15:04:00 | Glencourse (Kelani Ganga) | 15.26 | 🟡 Alert | 0.227 | 🔺 Rising |
| 2026-09-20 15:03:44 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 15:03:38 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-20 15:03:18 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-09-20 15:03:18 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:03:18 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.421 |  |
| 2026-09-20 15:03:12 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 15:03:03 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | 0.134 | 🔺 Rising |
| 2026-09-20 15:03:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:52 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:51 | Hanwella (Kelani Ganga) | 5.14 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-09-20 15:02:33 | Magura (Kalu Ganga) | 5.29 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-09-20 15:02:31 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 15:02:25 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 15:02:20 | Norwood (Kelani Ganga) | 2.27 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | -0.484 |  |
| 2026-09-20 15:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:07 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:50 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:44 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 15:01:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:20 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | -0.242 |  |
| 2026-09-20 15:01:14 | Peradeniya (Mahaweli Ganga) | 7.00 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-09-20 15:01:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-20 15:00:37 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:00:30 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:00:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 15:01:14 | Peradeniya (Mahaweli Ganga) | 7.00 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-09-20 15:04:00 | Glencourse (Kelani Ganga) | 15.26 | 🟡 Alert | 0.227 | 🔺 Rising |
| 2026-09-20 15:03:03 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | 0.134 | 🔺 Rising |
| 2026-09-20 15:02:33 | Magura (Kalu Ganga) | 5.29 | 🟡 Alert | 0.105 | 🔺 Rising |
| 2026-09-20 15:07:12 | Thawalama (Gin Ganga) | 5.14 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-09-20 15:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 15:02:20 | Norwood (Kelani Ganga) | 2.27 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 15:06:01 | Rathnapura (Kalu Ganga) | 6.86 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-20 15:06:55 | Holombuwa (Kelani Ganga) | 3.10 | 🟡 Alert | -0.151 |  |
| 2026-09-20 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 3.50 | 🟡 Alert | -0.484 |  |
| 2026-09-20 15:02:51 | Hanwella (Kelani Ganga) | 5.14 | 🟢 Normal | 0.434 | 🔺 Rising |
| 2026-09-20 15:03:18 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-09-20 15:04:08 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-20 15:03:44 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 15:03:38 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-20 15:09:06 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-20 15:01:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-20 15:02:25 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 15:04:41 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 15:03:12 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 15:07:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-20 15:01:44 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 15:02:31 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 15:00:30 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:03:18 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:50 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:00:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:00:37 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:05:41 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:05:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:03:01 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:52 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:29:29 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:07 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:02:11 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 15:01:20 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | -0.242 |  |
| 2026-09-20 15:03:18 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.421 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)