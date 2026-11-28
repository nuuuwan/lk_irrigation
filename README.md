# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_13:16:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 13:16:37 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.063 |  |
| 2026-11-28 13:15:20 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:14:13 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-11-28 13:11:20 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.070 |  |
| 2026-11-28 13:09:15 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:08:54 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | -0.027 |  |
| 2026-11-28 13:08:48 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 13:08:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:08:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.046 |  |
| 2026-11-28 13:07:48 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.080 |  |
| 2026-11-28 13:07:45 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.062 |  |
| 2026-11-28 13:06:54 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:06:17 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-11-28 13:05:40 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.089 |  |
| 2026-11-28 13:05:28 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.039 |  |
| 2026-11-28 13:05:27 | Moragaswewa (Deduru Oya) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-28 13:04:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-11-28 13:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:03:54 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:35 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:03:25 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:11 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.040 |  |
| 2026-11-28 13:03:07 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:02:48 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:02:38 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.121 |  |
| 2026-11-28 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.021 |  |
| 2026-11-28 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.245 |  |
| 2026-11-28 13:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-28 13:01:45 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.145 |  |
| 2026-11-28 13:01:37 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 13:01:33 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:01:11 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:01:09 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.155 |  |
| 2026-11-28 13:00:49 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.203 |  |
| 2026-11-28 13:00:35 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-11-28 13:00:33 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 12:02:58 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 12:08:47 | Moraketiya (Walawe Ganga) | 3.13 | 🟡 Alert | -0.018 |  |
| 2026-11-28 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | -0.021 |  |
| 2026-11-28 13:03:11 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.040 |  |
| 2026-11-28 13:04:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-11-28 13:05:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-28 13:01:37 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 13:08:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:01:11 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:25 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:03:54 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:00:33 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:09:15 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:01:33 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:15:20 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 13:14:13 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-11-28 13:06:17 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-11-28 13:04:17 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:03:07 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:03:35 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-28 13:00:35 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-11-28 13:06:54 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:02:48 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:05:27 | Moragaswewa (Deduru Oya) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-11-28 13:08:48 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 13:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-28 13:08:54 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | -0.027 |  |
| 2026-11-28 13:05:28 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.039 |  |
| 2026-11-28 13:08:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.046 |  |
| 2026-11-28 13:07:45 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.062 |  |
| 2026-11-28 13:16:37 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.063 |  |
| 2026-11-28 13:11:20 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.070 |  |
| 2026-11-28 13:07:48 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.080 |  |
| 2026-11-28 13:05:40 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.089 |  |
| 2026-11-28 13:02:38 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.121 |  |
| 2026-11-28 13:01:45 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.145 |  |
| 2026-11-28 13:01:09 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.155 |  |
| 2026-11-28 13:00:49 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.203 |  |
| 2026-11-28 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)