# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_10:07:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Nawalapitiya — Major Flood; 🟡 Rathnapura — Alert; 🟡 Norwood — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 10:07:55 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.598 | 🔺 Rising |
| 2026-09-20 10:06:53 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-09-20 10:06:12 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 10:05:48 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 1.094 | 🔺 Rising |
| 2026-09-20 10:05:30 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 1.009 | 🔺 Rising |
| 2026-09-20 10:05:17 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-20 10:05:03 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-09-20 10:04:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-09-20 10:04:43 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 10:04:37 | Thawalama (Gin Ganga) | 4.35 | 🟡 Alert | 0.497 | 🔺 Rising |
| 2026-09-20 10:04:33 | Baddegama (Gin Ganga) | 2.86 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-20 10:04:07 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-09-20 10:03:56 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 10:03:50 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 10:03:43 | Norwood (Kelani Ganga) | 1.95 | 🟡 Alert | 0.544 | 🔺 Rising |
| 2026-09-20 10:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-09-20 10:02:52 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 1.075 | 🔺 Rising |
| 2026-09-20 10:02:52 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.207 | 🔺 Rising |
| 2026-09-20 10:02:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-20 10:02:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:02:39 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:02:32 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 6.05 | 🔴 Major Flood | 0.050 | 🔺 Rising |
| 2026-09-20 10:02:10 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-20 10:02:04 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:53 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-09-20 10:01:34 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 10:01:23 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:17 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.801 | 🔺 Rising |
| 2026-09-20 10:01:17 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:43 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 10:00:34 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:00:30 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 6.05 | 🔴 Major Flood | 0.050 | 🔺 Rising |
| 2026-09-20 10:05:30 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 1.009 | 🔺 Rising |
| 2026-09-20 10:03:43 | Norwood (Kelani Ganga) | 1.95 | 🟡 Alert | 0.544 | 🔺 Rising |
| 2026-09-20 10:04:37 | Thawalama (Gin Ganga) | 4.35 | 🟡 Alert | 0.497 | 🔺 Rising |
| 2026-09-20 10:02:52 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | 0.207 | 🔺 Rising |
| 2026-09-20 10:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-09-20 10:05:48 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 1.094 | 🔺 Rising |
| 2026-09-20 10:02:52 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 1.075 | 🔺 Rising |
| 2026-09-20 10:01:17 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.801 | 🔺 Rising |
| 2026-09-20 10:07:55 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.598 | 🔺 Rising |
| 2026-09-20 10:06:53 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-09-20 10:05:03 | Deraniyagala (Kelani Ganga) | 3.09 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-09-20 09:05:24 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-09-20 10:05:17 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-20 10:04:07 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-09-20 10:02:10 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-20 10:04:33 | Baddegama (Gin Ganga) | 2.86 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-20 10:03:56 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 10:02:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-20 10:03:50 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 10:01:34 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 10:06:12 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 10:00:43 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 10:04:43 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 10:01:53 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:16 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:30 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:00:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:02:04 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:23 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:01:17 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:02:39 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 10:02:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:00:34 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:02:32 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-20 10:01:42 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-09-20 10:04:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)