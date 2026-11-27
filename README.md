# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_21:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,378 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 21:03:23 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-27 21:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.021 |  |
| 2026-11-27 21:03:11 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-27 21:03:01 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 21:03:00 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:02:55 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 21:02:55 | Dunamale (Aththanagalu Oya) | 3.49 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 21:02:46 | Moraketiya (Walawe Ganga) | 3.71 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-11-27 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-27 21:02:23 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-11-27 21:02:10 | Kuda Oya (Kirindi Oya) | 3.55 | 🟢 Normal | 1.071 | 🔺 Rising |
| 2026-11-27 21:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:01:55 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.209 |  |
| 2026-11-27 21:00:13 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 21:00:10 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 21:02:46 | Moraketiya (Walawe Ganga) | 3.71 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-11-27 21:02:55 | Dunamale (Aththanagalu Oya) | 3.49 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 21:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.021 |  |
| 2026-11-27 21:02:10 | Kuda Oya (Kirindi Oya) | 3.55 | 🟢 Normal | 1.071 | 🔺 Rising |
| 2026-11-27 20:06:36 | Holombuwa (Kelani Ganga) | 2.15 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-11-27 21:03:11 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-11-27 20:03:19 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-27 21:03:23 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-27 20:12:29 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-27 21:02:55 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 20:02:06 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-27 20:05:02 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-27 21:00:13 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 21:03:01 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-27 20:05:30 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 20:02:44 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-27 20:05:09 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-27 21:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:50 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:07:26 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:06:10 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:55 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:15:23 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 21:03:00 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-27 21:00:10 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-27 20:04:47 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-11-27 20:08:33 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-11-27 20:05:21 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.019 |  |
| 2026-11-27 20:07:18 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.019 |  |
| 2026-11-27 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-27 20:04:47 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.030 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 21:02:23 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-27 20:12:38 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | -0.102 |  |
| 2026-11-27 20:07:06 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.151 |  |
| 2026-11-27 20:05:37 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.184 |  |
| 2026-11-27 21:01:55 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)