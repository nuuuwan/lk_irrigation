# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_06:32:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,624 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 06:32:28 | Galgamuwa (Mee Oya) | 2.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-22 06:10:48 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-22 06:09:22 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-22 06:08:50 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 06:08:46 | Glencourse (Kelani Ganga) | 13.33 | 🟢 Normal | -0.253 |  |
| 2026-10-22 06:07:26 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.629 | 🔺 Rising |
| 2026-10-22 06:06:43 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.121 |  |
| 2026-10-22 06:06:18 | Moragaswewa (Deduru Oya) | 4.05 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-22 06:06:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:06:04 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -36.000 |  |
| 2026-10-22 06:06:03 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -36.000 |  |
| 2026-10-22 06:06:02 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -36.000 |  |
| 2026-10-22 06:06:01 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -36.000 |  |
| 2026-10-22 06:05:25 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.098 |  |
| 2026-10-22 06:05:06 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:04:37 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.254 |  |
| 2026-10-22 06:04:30 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.104 |  |
| 2026-10-22 06:04:21 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-22 06:04:08 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 06:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-22 06:04:01 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-10-22 06:03:59 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-22 06:03:37 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.629 | 🔺 Rising |
| 2026-10-22 06:03:27 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.277 |  |
| 2026-10-22 06:02:56 | Rathnapura (Kalu Ganga) | 5.41 | 🟡 Alert | -0.063 |  |
| 2026-10-22 06:02:44 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-22 06:02:33 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:02:24 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.524 |  |
| 2026-10-22 06:02:14 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-22 06:02:09 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.080 |  |
| 2026-10-22 06:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-10-22 06:01:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:01:47 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-10-22 06:01:37 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:01:36 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:01:33 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-22 06:01:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-10-22 06:01:22 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-22 06:01:14 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-22 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-22 05:59:37 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 06:02:56 | Rathnapura (Kalu Ganga) | 5.41 | 🟡 Alert | -0.063 |  |
| 2026-10-22 06:07:26 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.629 | 🔺 Rising |
| 2026-10-22 06:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-22 06:06:18 | Moragaswewa (Deduru Oya) | 4.05 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-22 06:02:44 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-22 06:01:22 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-22 06:08:50 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 06:03:59 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-22 06:10:48 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-22 04:06:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 06:01:14 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-22 06:02:14 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-22 06:04:21 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-22 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-22 06:09:22 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-22 06:32:28 | Galgamuwa (Mee Oya) | 2.27 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 06:01:33 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-22 06:01:37 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:06:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:01:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:02:33 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:05:06 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 05:10:18 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-22 06:01:47 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-10-22 06:04:08 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 06:04:01 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-10-22 06:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-10-22 06:01:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-10-22 05:59:37 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-10-22 06:02:09 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.080 |  |
| 2026-10-22 06:05:25 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.098 |  |
| 2026-10-22 06:04:30 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.104 |  |
| 2026-10-22 06:06:43 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.121 |  |
| 2026-10-22 06:08:46 | Glencourse (Kelani Ganga) | 13.33 | 🟢 Normal | -0.253 |  |
| 2026-10-22 06:04:37 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.254 |  |
| 2026-10-22 06:03:27 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.277 |  |
| 2026-10-22 06:02:24 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.524 |  |
| 2026-10-22 06:06:04 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)