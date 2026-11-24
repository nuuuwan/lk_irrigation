# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_00:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,854 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 00:03:15 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 00:03:14 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 00:03:13 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.063 |  |
| 2026-11-25 00:03:12 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-25 00:02:59 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-25 00:02:50 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-11-25 00:02:41 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-11-25 00:02:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-25 00:02:32 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-11-25 00:02:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 00:02:04 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-25 00:00:55 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.000 |  |
| 2026-11-25 00:00:38 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-25 00:00:22 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 00:02:59 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-25 00:00:55 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.000 |  |
| 2026-11-24 23:09:50 | Pitabeddara (Nilwala Ganga) | 3.93 | 🟢 Normal | 16.428 | 🔺 Rising |
| 2026-11-24 23:00:57 | Siyambalanduwa (Heda Oya) | 1.99 | 🟢 Normal | 0.838 | 🔺 Rising |
| 2026-11-25 00:02:32 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-11-24 23:04:18 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-25 00:02:41 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-11-25 00:00:38 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-24 23:03:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-24 22:05:23 | Urawa (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-24 23:03:27 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-24 23:03:21 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-24 23:09:46 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-24 23:10:09 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 23:04:00 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-25 00:03:12 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-25 00:02:04 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 22:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-25 00:03:15 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 00:03:14 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 21:01:08 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 23:03:21 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 23:03:16 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 23:05:28 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 23:07:39 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-25 00:02:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 00:00:22 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-24 23:00:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-24 23:04:47 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-11-25 00:02:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 23:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-11-25 00:03:13 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.063 |  |
| 2026-11-25 00:02:50 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-11-24 23:09:16 | Holombuwa (Kelani Ganga) | 1.84 | 🟢 Normal | -0.160 |  |
| 2026-11-24 22:30:21 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -1.256 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)