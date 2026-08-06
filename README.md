# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_06:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,225 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 06:18:08 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-06 06:15:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:10:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-06 06:09:21 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-08-06 06:08:23 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.096 |  |
| 2026-08-06 06:08:10 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-08-06 06:07:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.028 |  |
| 2026-08-06 06:07:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:07:22 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.056 |  |
| 2026-08-06 06:06:46 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.066 |  |
| 2026-08-06 06:06:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:53 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.027 |  |
| 2026-08-06 06:04:48 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 06:04:44 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:23 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-06 06:04:18 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:10 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-08-06 06:03:57 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.042 |  |
| 2026-08-06 06:03:54 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:03:48 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | -0.030 |  |
| 2026-08-06 06:03:21 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:03:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:03:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:02:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:02:25 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-06 06:02:08 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.086 |  |
| 2026-08-06 06:02:04 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 06:01:53 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:01:43 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-06 06:01:37 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:01:14 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:01:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-06 06:01:01 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:00:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.061 |  |
| 2026-08-06 06:00:29 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-08-06 05:42:32 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 06:01:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-06 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-06 06:10:13 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-06 06:02:04 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 06:04:48 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 06:18:08 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-06 06:04:23 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-06 06:01:14 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:03:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:07:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:02:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:44 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:06:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:15:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:04:18 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:03:21 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:01:01 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:01:53 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 06:08:10 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-08-06 06:03:54 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:02:25 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:03:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:01:37 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-08-06 06:00:29 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-08-06 06:01:43 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-06 06:04:53 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.027 |  |
| 2026-08-06 06:07:27 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.028 |  |
| 2026-08-06 06:09:21 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-08-06 06:03:48 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | -0.030 |  |
| 2026-08-06 06:03:57 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.042 |  |
| 2026-08-06 06:07:22 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.056 |  |
| 2026-08-06 06:00:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.061 |  |
| 2026-08-06 06:06:46 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.066 |  |
| 2026-08-06 06:04:10 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-08-06 06:02:08 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.086 |  |
| 2026-08-06 06:08:23 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)