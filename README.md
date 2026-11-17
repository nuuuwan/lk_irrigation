# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_05:40:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,993 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 05:40:18 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:18:04 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.154 |  |
| 2026-11-17 05:15:48 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:12:25 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:12:03 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:11:52 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:11:27 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-17 05:11:04 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.093 |  |
| 2026-11-17 05:10:23 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-17 05:08:46 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.021 |  |
| 2026-11-17 05:08:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-17 05:08:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-11-17 05:07:06 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:05:07 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:04:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:04:55 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-17 05:04:46 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:04:38 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.093 |  |
| 2026-11-17 05:04:32 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:04:27 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:03:45 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-17 05:03:17 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:03:13 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:02:54 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-11-17 05:02:46 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.099 |  |
| 2026-11-17 05:02:42 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:02:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 05:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:02:11 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.086 |  |
| 2026-11-17 05:02:06 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 05:02:03 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.055 |  |
| 2026-11-17 05:02:01 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:02:00 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:01:17 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.063 |  |
| 2026-11-17 05:01:13 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:01:10 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 05:08:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-17 05:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-17 05:10:23 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-17 05:04:55 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-17 05:02:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 05:02:06 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 05:01:13 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:02:01 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:04:27 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:11:27 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:02:42 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:03:17 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:01:10 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:11:52 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:40:18 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:04:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:07:06 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:15:48 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:12:25 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 02:01:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 05:04:46 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:04:32 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:02:00 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:05:07 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:03:13 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.010 |  |
| 2026-11-17 05:08:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-11-17 05:03:45 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-17 05:08:46 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.021 |  |
| 2026-11-17 05:02:54 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-17 05:02:03 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.055 |  |
| 2026-11-17 05:01:17 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.063 |  |
| 2026-11-17 05:02:11 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.086 |  |
| 2026-11-17 05:11:04 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.093 |  |
| 2026-11-17 05:02:46 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.099 |  |
| 2026-11-17 05:18:04 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)