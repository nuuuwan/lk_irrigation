# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_19:02:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 19:02:57 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.111 |  |
| 2026-11-08 19:02:23 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:22 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:21 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-08 19:02:15 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:13 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-08 19:01:45 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.081 |  |
| 2026-11-08 19:01:43 | Holombuwa (Kelani Ganga) | 3.90 | 🟠 Minor Flood | 0.611 | 🔺 Rising |
| 2026-11-08 19:01:28 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | -0.021 |  |
| 2026-11-08 19:01:24 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-08 19:01:21 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-08 19:01:16 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-11-08 19:01:02 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-11-08 19:01:00 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 19:00:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 19:01:43 | Holombuwa (Kelani Ganga) | 3.90 | 🟠 Minor Flood | 0.611 | 🔺 Rising |
| 2026-11-08 18:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.45 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-08 18:00:19 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 19:01:28 | Moraketiya (Walawe Ganga) | 3.10 | 🟡 Alert | -0.021 |  |
| 2026-11-08 18:02:38 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.024 |  |
| 2026-11-08 18:05:11 | Panadugama (Nilwala Ganga) | 5.51 | 🟡 Alert | -0.063 |  |
| 2026-11-08 18:03:20 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | 0.849 | 🔺 Rising |
| 2026-11-08 18:03:50 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.773 | 🔺 Rising |
| 2026-11-08 19:01:16 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-11-08 18:02:28 | Ellagawa (Kalu Ganga) | 7.86 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-08 19:02:21 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-08 18:03:41 | Magura (Kalu Ganga) | 3.14 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 19:00:11 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 19:01:00 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 18:00:42 | Moragaswewa (Deduru Oya) | 3.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 18:01:18 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-08 18:01:26 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 18:02:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-08 19:02:15 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:03:38 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:07:43 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:10:20 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 19:02:23 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:05:47 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-11-08 19:01:21 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 19:02:13 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:03:08 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:06:58 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.040 |  |
| 2026-11-08 19:01:02 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.041 |  |
| 2026-11-08 18:03:31 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.041 |  |
| 2026-11-08 19:01:24 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-08 17:07:39 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.058 |  |
| 2026-11-08 19:01:45 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.081 |  |
| 2026-11-08 19:02:57 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.111 |  |
| 2026-11-08 18:09:06 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.117 |  |
| 2026-11-08 18:01:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)