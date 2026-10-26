# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_10:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 10:08:39 | Rathnapura (Kalu Ganga) | 6.70 | 🟡 Alert | 0.584 | 🔺 Rising |
| 2026-10-26 10:08:32 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:07:56 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:07:30 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-26 10:07:23 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-26 10:06:43 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.052 |  |
| 2026-10-26 10:06:27 | Holombuwa (Kelani Ganga) | 2.98 | 🟢 Normal | 1.259 | 🔺 Rising |
| 2026-10-26 10:06:25 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-26 10:06:24 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-26 10:06:03 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.023 |  |
| 2026-10-26 10:05:54 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-26 10:05:51 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-10-26 10:05:37 | Hanwella (Kelani Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:05:17 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 10:05:08 | Hanwella (Kelani Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:04:42 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-26 10:04:39 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:04:19 | Norwood (Kelani Ganga) | 1.79 | 🟡 Alert | 0.141 | 🔺 Rising |
| 2026-10-26 10:04:10 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 10:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-26 10:03:44 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:03:44 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:03:35 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-26 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-26 10:03:24 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.75 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-10-26 10:02:38 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:02:37 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.032 |  |
| 2026-10-26 10:02:37 | Moragaswewa (Deduru Oya) | 4.26 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-26 10:02:23 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:02:09 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 10:01:48 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.072 |  |
| 2026-10-26 10:01:45 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-26 10:01:42 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:01:38 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-26 10:01:23 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 10:01:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:00:28 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 10:08:39 | Rathnapura (Kalu Ganga) | 6.70 | 🟡 Alert | 0.584 | 🔺 Rising |
| 2026-10-26 10:04:19 | Norwood (Kelani Ganga) | 1.79 | 🟡 Alert | 0.141 | 🔺 Rising |
| 2026-10-26 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.75 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-10-26 10:02:37 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.032 |  |
| 2026-10-26 10:06:27 | Holombuwa (Kelani Ganga) | 2.98 | 🟢 Normal | 1.259 | 🔺 Rising |
| 2026-10-26 10:05:51 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-10-26 10:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-26 10:04:42 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-26 10:01:45 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-26 10:07:30 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-26 10:05:54 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-26 10:02:37 | Moragaswewa (Deduru Oya) | 4.26 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-26 09:06:26 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-26 10:06:24 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-26 10:03:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-26 10:01:23 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 10:00:28 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-26 10:01:38 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-26 10:03:24 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 10:02:09 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 10:04:10 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 10:07:23 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-26 10:05:17 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 10:06:25 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-26 10:03:44 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:07:56 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:05:37 | Hanwella (Kelani Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:01:18 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:04:39 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:02:23 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:03:44 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:02:38 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:08:32 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:01:42 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:03:35 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-26 10:06:03 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | -0.023 |  |
| 2026-10-26 09:07:27 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.038 |  |
| 2026-10-26 10:06:43 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.052 |  |
| 2026-10-26 10:01:48 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)