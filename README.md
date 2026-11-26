# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_01:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,632 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 01:03:31 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 01:03:11 | Giriulla (Maha Oya) | 4.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-27 01:02:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 01:02:34 | Kuda Oya (Kirindi Oya) | 3.33 | 🟢 Normal | -0.203 |  |
| 2026-11-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | -0.112 |  |
| 2026-11-27 01:02:30 | Nakkala (Kumbukkan Oya) | 1.80 | 🟢 Normal | -0.150 |  |
| 2026-11-27 01:02:04 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | -0.021 |  |
| 2026-11-27 01:01:39 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-27 01:01:37 | Siyambalanduwa (Heda Oya) | 2.55 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-27 01:01:36 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-11-27 01:01:29 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.035 |  |
| 2026-11-27 01:00:20 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 00:07:57 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-27 00:03:25 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-27 00:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-11-27 00:06:26 | Moraketiya (Walawe Ganga) | 4.00 | 🟡 Alert | -0.102 |  |
| 2026-11-27 00:08:49 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-11-27 00:08:17 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-27 01:01:37 | Siyambalanduwa (Heda Oya) | 2.55 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-27 01:03:11 | Giriulla (Maha Oya) | 4.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-26 23:06:02 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-27 00:05:59 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-27 01:01:39 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-27 00:05:34 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 00:03:19 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-27 01:03:31 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-27 00:03:40 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 00:06:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 00:02:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:01:24 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:04:34 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:03:46 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-27 00:07:30 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-27 01:02:04 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 00:00:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-11-27 00:03:01 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-11-27 01:01:36 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-11-27 01:01:29 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.035 |  |
| 2026-11-27 01:02:35 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 01:00:20 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-11-27 00:05:54 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.068 |  |
| 2026-11-27 00:07:55 | Thanamalwila (Kirindi Oya) | 3.33 | 🟢 Normal | -0.077 |  |
| 2026-11-27 00:04:46 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.094 |  |
| 2026-11-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | -0.112 |  |
| 2026-11-27 00:05:59 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.143 |  |
| 2026-11-27 01:02:30 | Nakkala (Kumbukkan Oya) | 1.80 | 🟢 Normal | -0.150 |  |
| 2026-11-27 01:02:34 | Kuda Oya (Kirindi Oya) | 3.33 | 🟢 Normal | -0.203 |  |
| 2026-11-27 00:10:53 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.260 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)