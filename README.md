# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_20:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,173 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 20:03:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 20:03:12 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-11 20:03:11 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-11-11 20:02:55 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 20:02:45 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-11 20:02:30 | Holombuwa (Kelani Ganga) | 2.23 | 🟢 Normal | -0.082 |  |
| 2026-11-11 20:02:29 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-11-11 20:02:27 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-11 20:02:26 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 20:01:50 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 20:01:04 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.064 |  |
| 2026-11-11 20:00:46 | Wellawaya (Kirindi Oya) | 2.12 | 🟢 Normal | 0.497 | 🔺 Rising |
| 2026-11-11 20:00:43 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:59:19 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -108.000 |  |
| 2026-11-11 19:59:17 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -108.000 |  |
| 2026-11-11 19:57:09 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 19:07:03 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 19:10:35 | Baddegama (Gin Ganga) | 4.08 | 🟠 Minor Flood | -0.019 |  |
| 2026-11-11 19:01:40 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.735 | 🔺 Rising |
| 2026-11-11 19:09:07 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.268 | 🔺 Rising |
| 2026-11-11 20:02:26 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 19:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.008 |  |
| 2026-11-11 19:05:48 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.010 |  |
| 2026-11-11 19:03:44 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-11 20:00:46 | Wellawaya (Kirindi Oya) | 2.12 | 🟢 Normal | 0.497 | 🔺 Rising |
| 2026-11-11 19:06:52 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-11-11 19:06:54 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-11 19:03:30 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-11 19:06:21 | Deraniyagala (Kelani Ganga) | 3.32 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-11 20:01:50 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 20:02:45 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-11 19:05:21 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-11 20:03:12 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-11 19:02:35 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-11 19:03:34 | Moragaswewa (Deduru Oya) | 3.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-11 19:07:40 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 19:01:31 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 20:02:27 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-11 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:10:03 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 19:07:31 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 20:00:43 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-11 20:03:15 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 20:02:55 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 20:02:29 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-11-11 19:01:45 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-11-11 20:03:11 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-11-11 20:01:04 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.064 |  |
| 2026-11-11 20:02:30 | Holombuwa (Kelani Ganga) | 2.23 | 🟢 Normal | -0.082 |  |
| 2026-11-11 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |
| 2026-11-11 19:59:19 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)