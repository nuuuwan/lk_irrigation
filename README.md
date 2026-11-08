# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_16:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 16:02:56 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:02:47 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:32 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-08 16:02:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:01:44 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.070 |  |
| 2026-11-08 16:01:41 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.021 |  |
| 2026-11-08 16:01:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:01:24 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-11-08 16:00:43 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 15:02:05 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-08 15:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.011 |  |
| 2026-11-08 16:01:41 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.021 |  |
| 2026-11-08 15:04:44 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | -0.061 |  |
| 2026-11-08 15:05:17 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.066 |  |
| 2026-11-08 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-08 15:02:09 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-11-08 15:07:37 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 15:03:56 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-08 15:04:42 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-08 15:02:28 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 15:03:56 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-08 16:02:32 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 15:06:49 | Ellagawa (Kalu Ganga) | 7.48 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-08 15:00:56 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 15:01:08 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 15:01:11 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:47 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:07:50 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:02:27 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:04:42 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:01:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:56 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:02:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:01:24 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-11-08 15:05:14 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-11-08 15:10:15 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.017 |  |
| 2026-11-08 15:04:26 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-08 16:00:43 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-11-08 15:06:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-11-08 15:02:33 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.040 |  |
| 2026-11-08 15:02:51 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.050 |  |
| 2026-11-08 16:01:44 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.070 |  |
| 2026-11-08 15:02:48 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.080 |  |
| 2026-11-08 15:04:16 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-11-08 15:03:36 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.113 |  |
| 2026-11-08 15:06:15 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.126 |  |
| 2026-11-08 15:04:53 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)