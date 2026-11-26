# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_18:07:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 18:07:17 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.029 |  |
| 2026-11-26 18:06:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-11-26 18:06:29 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-26 18:06:05 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-11-26 18:05:40 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 18:04:59 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-26 18:04:55 | Moragaswewa (Deduru Oya) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-26 18:04:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-26 18:04:12 | Giriulla (Maha Oya) | 2.62 | 🟢 Normal | -0.060 |  |
| 2026-11-26 18:04:03 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-26 18:03:56 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-26 18:03:46 | Magura (Kalu Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-26 18:03:11 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-11-26 18:03:09 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.022 |  |
| 2026-11-26 18:03:03 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-26 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-26 18:02:54 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:02:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-26 18:02:26 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-26 18:02:24 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:01:46 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:01:30 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.044 |  |
| 2026-11-26 18:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.095 |  |
| 2026-11-26 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-11-26 18:01:14 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.060 |  |
| 2026-11-26 18:01:05 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.026 |  |
| 2026-11-26 18:00:49 | Magura (Kalu Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 18:00:17 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2026-11-26 18:00:08 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-26 17:59:26 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-26 18:03:46 | Magura (Kalu Ganga) | 4.12 | 🟡 Alert | 0.000 |  |
| 2026-11-26 17:02:50 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.067 |  |
| 2026-11-26 17:07:19 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-11-26 17:04:56 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-26 18:02:29 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-26 18:03:11 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-11-26 18:03:56 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-26 18:06:05 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-11-26 17:07:14 | Moraketiya (Walawe Ganga) | 2.87 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-26 18:02:26 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-26 18:04:03 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-26 18:03:03 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-26 18:04:59 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-26 18:04:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-26 18:04:55 | Moragaswewa (Deduru Oya) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-26 18:02:24 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 18:06:29 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-26 18:00:08 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-26 18:02:54 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 17:59:26 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 18:05:40 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 17:18:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:01:46 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:06:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-11-26 17:13:53 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:03:09 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.022 |  |
| 2026-11-26 18:00:17 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2026-11-26 18:01:05 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.026 |  |
| 2026-11-26 18:07:17 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.029 |  |
| 2026-11-26 17:15:47 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.038 |  |
| 2026-11-26 18:01:30 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.044 |  |
| 2026-11-26 18:04:12 | Giriulla (Maha Oya) | 2.62 | 🟢 Normal | -0.060 |  |
| 2026-11-26 18:01:14 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.060 |  |
| 2026-11-26 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-11-26 18:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)