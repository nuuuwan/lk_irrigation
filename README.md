# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_19:03:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Holombuwa — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 19:03:43 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 19:03:28 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-26 19:03:25 | Dunamale (Aththanagalu Oya) | 3.35 | 🟡 Alert | 0.000 |  |
| 2026-11-26 19:03:06 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-26 19:03:00 | Moragaswewa (Deduru Oya) | 4.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-26 19:02:58 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | 0.871 | 🔺 Rising |
| 2026-11-26 19:02:19 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-11-26 19:01:55 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.049 |  |
| 2026-11-26 19:01:48 | Holombuwa (Kelani Ganga) | 3.00 | 🟡 Alert | 0.612 | 🔺 Rising |
| 2026-11-26 19:01:40 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 19:01:40 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-26 18:30:57 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 18:08:30 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.617 | 🔺 Rising |
| 2026-11-26 19:01:48 | Holombuwa (Kelani Ganga) | 3.00 | 🟡 Alert | 0.612 | 🔺 Rising |
| 2026-11-26 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-26 18:03:46 | Magura (Kalu Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-26 19:03:25 | Dunamale (Aththanagalu Oya) | 3.35 | 🟡 Alert | 0.000 |  |
| 2026-11-26 19:02:58 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | 0.871 | 🔺 Rising |
| 2026-11-26 19:01:40 | Wellawaya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-26 18:03:56 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-26 18:06:05 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-11-26 18:02:26 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-26 18:04:03 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-26 19:03:28 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-26 18:08:06 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-26 18:04:59 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-26 18:04:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-26 19:03:06 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-26 19:03:00 | Moragaswewa (Deduru Oya) | 4.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-26 19:01:40 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 19:03:43 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 18:05:40 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 18:08:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:14:21 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:13:28 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:08:25 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:01:46 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:06:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-11-26 19:02:19 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:03:09 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.022 |  |
| 2026-11-26 18:30:57 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.024 |  |
| 2026-11-26 18:01:05 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.026 |  |
| 2026-11-26 18:07:17 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.029 |  |
| 2026-11-26 18:01:30 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.044 |  |
| 2026-11-26 19:01:55 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.049 |  |
| 2026-11-26 18:04:12 | Giriulla (Maha Oya) | 2.62 | 🟢 Normal | -0.060 |  |
| 2026-11-26 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-11-26 18:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)