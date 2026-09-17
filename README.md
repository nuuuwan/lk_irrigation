# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_13:32:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 13:32:05 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 13:13:48 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-09-17 13:12:49 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.017 |  |
| 2026-09-17 13:12:03 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 13:11:53 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:10:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:09:34 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:08:13 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 13:08:07 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-17 13:07:43 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-17 13:07:38 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:06:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:05:13 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 13:05:06 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:52 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:26 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:04:24 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 13:04:18 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:04:14 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:10 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.297 | 🔺 Rising |
| 2026-09-17 13:04:07 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 13:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:58 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:49 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-09-17 13:02:44 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:43 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-17 13:02:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:24 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-17 13:02:00 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-09-17 13:01:58 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 13:01:25 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-17 13:01:12 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:01:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:00:41 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:00:34 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:00:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 13:04:10 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.297 | 🔺 Rising |
| 2026-09-17 13:05:13 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 13:07:43 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-17 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-17 13:02:43 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-17 13:08:07 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-17 13:32:05 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 13:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-17 13:04:07 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 13:04:24 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 13:08:13 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 13:01:58 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 13:12:03 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 13:00:08 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:24 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:01:12 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:58 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:00:34 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:05:06 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:10:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:03:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:00:41 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:01:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:07:38 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:14 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:04:52 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:06:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:11:53 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:44 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-17 13:02:00 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-09-17 13:13:48 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-09-17 13:04:26 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:04:18 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:01:25 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-17 13:12:49 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.017 |  |
| 2026-09-17 13:02:49 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)