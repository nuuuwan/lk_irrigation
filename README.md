# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_05:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 05:03:31 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 05:03:18 | Giriulla (Maha Oya) | 4.40 | 🟢 Normal | -0.108 |  |
| 2026-11-27 05:03:04 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-27 05:03:02 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-11-27 05:03:02 | Siyambalanduwa (Heda Oya) | 2.19 | 🟢 Normal | -0.106 |  |
| 2026-11-27 05:02:46 | Moragaswewa (Deduru Oya) | 3.80 | 🟢 Normal | -0.303 |  |
| 2026-11-27 05:02:40 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-11-27 05:02:28 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-11-27 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-11-27 05:01:49 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-27 05:01:12 | Moraketiya (Walawe Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-11-27 05:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-11-27 05:01:07 | Nakkala (Kumbukkan Oya) | 1.80 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-11-27 05:01:01 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-27 04:37:37 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | 0.383 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 04:03:45 | Magura (Kalu Ganga) | 5.70 | 🟡 Alert | 1.110 | 🔺 Rising |
| 2026-11-27 05:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-11-27 04:02:20 | Dunamale (Aththanagalu Oya) | 3.85 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-27 05:01:12 | Moraketiya (Walawe Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-11-27 05:01:07 | Nakkala (Kumbukkan Oya) | 1.80 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-11-27 04:05:35 | Badalgama (Maha Oya) | 4.85 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-27 04:07:18 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-27 05:01:49 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-27 04:13:26 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-27 05:03:31 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 05:03:04 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-27 04:01:32 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-27 04:07:58 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-27 04:03:39 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 03:06:00 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-27 04:10:33 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 04:05:37 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:50 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 05:02:28 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:04:44 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:12 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:09:16 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 02:06:39 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-27 05:01:01 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-27 04:07:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.017 |  |
| 2026-11-27 05:02:40 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 03:04:43 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.024 |  |
| 2026-11-27 04:16:18 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.025 |  |
| 2026-11-27 05:03:02 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-11-27 04:08:15 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-11-27 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-11-27 04:02:10 | Kuda Oya (Kirindi Oya) | 2.79 | 🟢 Normal | -0.092 |  |
| 2026-11-27 05:03:02 | Siyambalanduwa (Heda Oya) | 2.19 | 🟢 Normal | -0.106 |  |
| 2026-11-27 05:03:18 | Giriulla (Maha Oya) | 4.40 | 🟢 Normal | -0.108 |  |
| 2026-11-27 03:10:28 | Thanamalwila (Kirindi Oya) | 2.68 | 🟢 Normal | -0.210 |  |
| 2026-11-27 05:02:46 | Moragaswewa (Deduru Oya) | 3.80 | 🟢 Normal | -0.303 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)