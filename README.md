# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_00:10:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 00:10:53 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.260 |  |
| 2026-11-27 00:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-11-27 00:09:50 | Wellawaya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-27 00:08:49 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:08:49 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-11-27 00:08:17 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-27 00:07:57 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-27 00:07:55 | Thanamalwila (Kirindi Oya) | 3.33 | 🟢 Normal | -0.077 |  |
| 2026-11-27 00:07:30 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-27 00:06:53 | Giriulla (Maha Oya) | 4.50 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-27 00:06:26 | Moraketiya (Walawe Ganga) | 4.00 | 🟡 Alert | -0.102 |  |
| 2026-11-27 00:06:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 00:05:59 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-27 00:05:59 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.143 |  |
| 2026-11-27 00:05:54 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.068 |  |
| 2026-11-27 00:05:34 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 00:05:10 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | 0.619 | 🔺 Rising |
| 2026-11-27 00:04:46 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.094 |  |
| 2026-11-27 00:04:34 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:04:02 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-27 00:03:46 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:03:40 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 00:03:39 | Moragaswewa (Deduru Oya) | 4.62 | 🟢 Normal | -0.029 |  |
| 2026-11-27 00:03:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-27 00:03:25 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 00:03:24 | Kuda Oya (Kirindi Oya) | 3.53 | 🟢 Normal | -0.271 |  |
| 2026-11-27 00:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 00:03:01 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:02:48 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-11-27 00:02:41 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.156 |  |
| 2026-11-27 00:02:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-27 00:01:24 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:00:35 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.641 |  |
| 2026-11-27 00:00:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 00:07:57 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-27 00:03:25 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 00:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-11-27 00:06:26 | Moraketiya (Walawe Ganga) | 4.00 | 🟡 Alert | -0.102 |  |
| 2026-11-27 00:05:10 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | 0.619 | 🔺 Rising |
| 2026-11-27 00:08:49 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-11-27 00:08:17 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-27 00:06:53 | Giriulla (Maha Oya) | 4.50 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-27 00:03:25 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-27 00:04:02 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-26 23:06:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-27 00:05:59 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-27 00:05:34 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 00:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 00:03:40 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 00:06:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-27 00:09:50 | Wellawaya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:01:24 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:04:34 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:08:49 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:03:46 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:07:30 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 00:00:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:03:01 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:03:39 | Moragaswewa (Deduru Oya) | 4.62 | 🟢 Normal | -0.029 |  |
| 2026-11-27 00:02:48 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-11-27 00:02:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-27 00:05:54 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.068 |  |
| 2026-11-27 00:07:55 | Thanamalwila (Kirindi Oya) | 3.33 | 🟢 Normal | -0.077 |  |
| 2026-11-27 00:04:46 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.094 |  |
| 2026-11-27 00:05:59 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.143 |  |
| 2026-11-27 00:02:41 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.156 |  |
| 2026-11-27 00:10:53 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.260 |  |
| 2026-11-27 00:03:24 | Kuda Oya (Kirindi Oya) | 3.53 | 🟢 Normal | -0.271 |  |
| 2026-11-27 00:00:35 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -0.641 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)