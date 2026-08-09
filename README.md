# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_18:14:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,980 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 18:14:07 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:11:43 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:10:53 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:08:40 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.028 |  |
| 2026-08-09 18:07:11 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 18:06:47 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:06:46 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:06:44 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:06:03 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 18:05:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:05:30 | Rathnapura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-08-09 18:04:57 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:48 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:48 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 18:04:42 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:17 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.035 |  |
| 2026-08-09 18:03:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.059 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:39 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:17 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:03:01 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:02:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.057 |  |
| 2026-08-09 18:02:49 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:02:40 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:02:37 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 18:02:23 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:02:12 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.020 |  |
| 2026-08-09 18:01:55 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 18:01:53 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-08-09 18:01:49 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-09 18:01:40 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-08-09 18:01:38 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:25 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:01:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:00:51 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.024 |  |
| 2026-08-09 18:00:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 18:05:30 | Rathnapura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-08-09 18:01:49 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-09 18:01:55 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 18:04:48 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 18:07:11 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 18:06:03 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:02:23 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:03:01 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:01:38 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:02:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:42 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:14:07 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:01:25 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:39 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:11:43 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:05:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:02:49 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:57 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:55 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:04:48 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:10:53 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:06:47 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:17 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:02:37 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:02:40 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-08-09 18:01:53 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-08-09 18:02:12 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.020 |  |
| 2026-08-09 18:00:51 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.024 |  |
| 2026-08-09 18:08:40 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.028 |  |
| 2026-08-09 18:04:17 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.035 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 18:01:40 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.049 |  |
| 2026-08-09 18:00:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.055 |  |
| 2026-08-09 18:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.057 |  |
| 2026-08-09 18:03:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)