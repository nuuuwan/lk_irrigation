# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_13:09:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Urawa — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 13:09:06 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:08:14 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.101 |  |
| 2026-10-15 13:07:09 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-15 13:06:40 | Urawa (Nilwala Ganga) | 2.79 | 🟡 Alert | 0.517 | 🔺 Rising |
| 2026-10-15 13:06:37 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.077 |  |
| 2026-10-15 13:06:25 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-15 13:06:21 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 13:06:16 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-15 13:06:09 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:05:20 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.047 |  |
| 2026-10-15 13:05:18 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 13:05:03 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 13:04:53 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.020 |  |
| 2026-10-15 13:04:50 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-15 13:04:44 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.121 |  |
| 2026-10-15 13:04:43 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 13:04:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:04:37 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.070 |  |
| 2026-10-15 13:04:30 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:04:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-10-15 13:03:38 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.019 |  |
| 2026-10-15 13:03:17 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.121 |  |
| 2026-10-15 13:03:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 13:03:11 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-15 13:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.010 |  |
| 2026-10-15 13:03:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.131 |  |
| 2026-10-15 13:02:43 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-10-15 13:02:36 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-15 13:02:23 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:01:27 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-10-15 13:01:26 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-15 13:01:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 13:01:10 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:00:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:00:42 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-15 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-15 13:00:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:59:12 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.801 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 13:06:16 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-15 13:06:40 | Urawa (Nilwala Ganga) | 2.79 | 🟡 Alert | 0.517 | 🔺 Rising |
| 2026-10-15 13:02:43 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-10-15 13:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | -0.010 |  |
| 2026-10-15 13:04:53 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.020 |  |
| 2026-10-15 12:59:12 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.801 | 🔺 Rising |
| 2026-10-15 13:01:27 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-10-15 13:02:36 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-15 13:07:09 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-15 13:03:11 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-15 13:01:26 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-15 13:06:25 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-15 13:06:21 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 13:05:18 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 13:03:15 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 13:04:50 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-15 13:04:43 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 13:05:03 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 13:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 13:00:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:09:06 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:01:10 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:02:23 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:04:30 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:04:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:01:22 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:00:43 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 13:00:42 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-15 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:18:06 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.014 |  |
| 2026-10-15 13:03:38 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.019 |  |
| 2026-10-15 13:05:20 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.047 |  |
| 2026-10-15 13:04:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-10-15 13:04:37 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | -0.070 |  |
| 2026-10-15 13:06:37 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.077 |  |
| 2026-10-15 13:08:14 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.101 |  |
| 2026-10-15 13:04:44 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.121 |  |
| 2026-10-15 13:03:17 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.121 |  |
| 2026-10-15 13:03:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)