# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_14:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Holombuwa — Major Flood; 🟠 Rathnapura — Minor Flood; 🟡 Panadugama — Alert; 🟡 Peradeniya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 14:16:19 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:12:38 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-10-26 14:11:39 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 14:11:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:10:33 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-10-26 14:10:01 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 14:09:13 | Pitabeddara (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-26 14:08:36 | Giriulla (Maha Oya) | 3.53 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-26 14:07:55 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-10-26 14:07:53 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-26 14:07:48 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | 2.467 | 🔺 Rising |
| 2026-10-26 14:07:09 | Peradeniya (Mahaweli Ganga) | 5.34 | 🟡 Alert | 0.355 | 🔺 Rising |
| 2026-10-26 14:06:53 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-26 14:06:24 | Nawalapitiya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.398 |  |
| 2026-10-26 14:06:01 | Galgamuwa (Mee Oya) | 3.75 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-10-26 14:05:50 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-10-26 14:05:35 | Rathnapura (Kalu Ganga) | 7.88 | 🟠 Minor Flood | 0.104 | 🔺 Rising |
| 2026-10-26 14:05:25 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-10-26 14:05:23 | Kithulgala (Kelani Ganga) | 3.00 | 🟡 Alert | -0.463 |  |
| 2026-10-26 14:05:18 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.046 |  |
| 2026-10-26 14:05:07 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:04:53 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:04:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:04:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:04:34 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:04:14 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-26 14:04:13 | Holombuwa (Kelani Ganga) | 5.19 | 🔴 Major Flood | 0.138 | 🔺 Rising |
| 2026-10-26 14:04:06 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-10-26 14:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-10-26 14:02:32 | Moragaswewa (Deduru Oya) | 4.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:02:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:02:13 | Norwood (Kelani Ganga) | 2.27 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-26 14:02:07 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.417 |  |
| 2026-10-26 14:01:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-26 14:01:39 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 14:01:12 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-10-26 14:01:03 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:00:56 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.013 |  |
| 2026-10-26 14:00:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 14:04:13 | Holombuwa (Kelani Ganga) | 5.19 | 🔴 Major Flood | 0.138 | 🔺 Rising |
| 2026-10-26 14:05:35 | Rathnapura (Kalu Ganga) | 7.88 | 🟠 Minor Flood | 0.104 | 🔺 Rising |
| 2026-10-26 14:07:48 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | 2.467 | 🔺 Rising |
| 2026-10-26 14:07:09 | Peradeniya (Mahaweli Ganga) | 5.34 | 🟡 Alert | 0.355 | 🔺 Rising |
| 2026-10-26 14:05:25 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-10-26 14:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-10-26 14:02:13 | Norwood (Kelani Ganga) | 2.27 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-26 14:11:39 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 14:05:23 | Kithulgala (Kelani Ganga) | 3.00 | 🟡 Alert | -0.463 |  |
| 2026-10-26 14:07:55 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-10-26 14:09:13 | Pitabeddara (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-26 14:06:01 | Galgamuwa (Mee Oya) | 3.75 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-10-26 14:04:06 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-10-26 14:08:36 | Giriulla (Maha Oya) | 3.53 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-26 14:05:50 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-10-26 14:04:14 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-26 14:06:53 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-26 14:10:01 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-26 14:01:48 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-26 14:07:53 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-26 14:01:39 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 14:04:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:04:34 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:02:32 | Moragaswewa (Deduru Oya) | 4.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 14:11:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:16:19 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:04:48 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:01:03 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:04:53 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:05:07 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:02:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-26 14:10:33 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-10-26 14:00:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-26 14:00:56 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.013 |  |
| 2026-10-26 14:12:38 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.018 |  |
| 2026-10-26 14:01:12 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-10-26 14:05:18 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.046 |  |
| 2026-10-26 14:06:24 | Nawalapitiya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.398 |  |
| 2026-10-26 14:02:07 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.417 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)