# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_11:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 11:03:14 | Moraketiya (Walawe Ganga) | 3.56 | 🟡 Alert | -0.203 |  |
| 2026-11-27 11:03:10 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:03:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-11-27 11:03:01 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:45 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.069 |  |
| 2026-11-27 11:02:43 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 11:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-11-27 11:02:31 | Kuda Oya (Kirindi Oya) | 2.57 | 🟢 Normal | -0.044 |  |
| 2026-11-27 11:02:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:26 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-11-27 11:02:24 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.020 |  |
| 2026-11-27 11:02:16 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 11:02:05 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:01:55 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 11:01:55 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.060 |  |
| 2026-11-27 11:01:46 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:01:36 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:19 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.066 |  |
| 2026-11-27 11:00:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:00:09 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:59:09 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 11:02:24 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.020 |  |
| 2026-11-27 11:01:55 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | -0.060 |  |
| 2026-11-27 11:03:14 | Moraketiya (Walawe Ganga) | 3.56 | 🟡 Alert | -0.203 |  |
| 2026-11-27 11:01:55 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 10:08:32 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 11:01:46 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 11:02:05 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:03:10 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:00:45 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 10:14:32 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-27 11:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:01:36 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-27 11:02:16 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-27 10:17:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:02:13 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:03:01 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:00:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-27 11:02:28 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-11-27 10:08:12 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.028 |  |
| 2026-11-27 11:02:26 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:04:16 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:05:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-27 10:59:09 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.034 |  |
| 2026-11-27 10:07:32 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-11-27 10:09:59 | Badalgama (Maha Oya) | 4.90 | 🟢 Normal | -0.039 |  |
| 2026-11-27 11:02:31 | Kuda Oya (Kirindi Oya) | 2.57 | 🟢 Normal | -0.044 |  |
| 2026-11-27 11:02:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2026-11-27 10:17:42 | Giriulla (Maha Oya) | 3.95 | 🟢 Normal | -0.057 |  |
| 2026-11-27 11:02:43 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 11:01:19 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.066 |  |
| 2026-11-27 11:03:08 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.067 |  |
| 2026-11-27 11:02:45 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.069 |  |
| 2026-11-27 09:04:33 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-11-27 10:02:39 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.122 |  |
| 2026-11-27 10:03:55 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.129 |  |
| 2026-11-27 10:04:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)