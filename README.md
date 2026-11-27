# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_17:20:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,250 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 17:20:44 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.048 |  |
| 2026-11-27 17:12:55 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-27 17:12:48 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.089 |  |
| 2026-11-27 17:08:15 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-27 17:08:05 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.018 |  |
| 2026-11-27 17:07:17 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 2.301 | 🔺 Rising |
| 2026-11-27 17:07:04 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-11-27 17:06:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 17:06:41 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-27 17:06:21 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-27 17:05:05 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.049 |  |
| 2026-11-27 17:04:51 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.058 |  |
| 2026-11-27 17:04:50 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:04:40 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:04:19 | Badalgama (Maha Oya) | 4.36 | 🟢 Normal | -0.064 |  |
| 2026-11-27 17:04:11 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-27 17:04:06 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.095 |  |
| 2026-11-27 17:03:48 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.070 |  |
| 2026-11-27 17:03:44 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:03:42 | Moraketiya (Walawe Ganga) | 3.07 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-27 17:03:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-11-27 17:03:09 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-11-27 17:03:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:02:59 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-27 17:02:47 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-27 17:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 17:02:21 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.080 |  |
| 2026-11-27 17:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-11-27 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | -0.010 |  |
| 2026-11-27 17:02:09 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-27 17:02:08 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.066 |  |
| 2026-11-27 17:02:03 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.062 |  |
| 2026-11-27 17:01:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:01:35 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.049 |  |
| 2026-11-27 17:01:22 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:01:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-11-27 17:01:10 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 17:03:42 | Moraketiya (Walawe Ganga) | 3.07 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-27 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | -0.010 |  |
| 2026-11-27 17:02:21 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.080 |  |
| 2026-11-27 17:07:17 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | 2.301 | 🔺 Rising |
| 2026-11-27 17:06:21 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-27 17:02:59 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-27 17:04:11 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-27 17:02:09 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-27 17:08:15 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-27 17:12:55 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-27 17:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 17:06:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 17:02:47 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 17:04:50 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:04:40 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:03:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:01:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:03:44 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:01:22 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-27 17:08:05 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | -0.018 |  |
| 2026-11-27 17:01:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-11-27 17:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-11-27 17:06:41 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-27 17:03:09 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-11-27 17:03:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-11-27 17:01:10 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.044 |  |
| 2026-11-27 17:20:44 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.048 |  |
| 2026-11-27 17:01:35 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.049 |  |
| 2026-11-27 17:05:05 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.049 |  |
| 2026-11-27 17:04:51 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.058 |  |
| 2026-11-27 17:07:04 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2026-11-27 17:02:03 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.062 |  |
| 2026-11-27 17:04:19 | Badalgama (Maha Oya) | 4.36 | 🟢 Normal | -0.064 |  |
| 2026-11-27 17:02:08 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.066 |  |
| 2026-11-27 17:03:48 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.070 |  |
| 2026-11-27 17:12:48 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.089 |  |
| 2026-11-27 17:04:06 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)