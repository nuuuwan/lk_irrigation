# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_03:08:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Moragaswewa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 03:08:02 | Holombuwa (Kelani Ganga) | 2.30 | 🟢 Normal | -0.099 |  |
| 2026-10-27 03:07:52 | Urawa (Nilwala Ganga) | 2.30 | 🟢 Normal | -19.636 |  |
| 2026-10-27 03:07:48 | Moraketiya (Walawe Ganga) | 2.38 | 🟢 Normal | -0.023 |  |
| 2026-10-27 03:07:35 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-27 03:07:30 | Urawa (Nilwala Ganga) | 2.42 | 🟢 Normal | -19.636 |  |
| 2026-10-27 03:07:24 | Pitabeddara (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:06:57 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-27 03:06:56 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-27 03:05:23 | Peradeniya (Mahaweli Ganga) | 4.24 | 🟢 Normal | -0.151 |  |
| 2026-10-27 03:04:42 | Baddegama (Gin Ganga) | 3.70 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 03:04:25 | Rathnapura (Kalu Ganga) | 8.68 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-10-27 03:04:18 | Norwood (Kelani Ganga) | 1.74 | 🟡 Alert | -0.021 |  |
| 2026-10-27 03:03:57 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-10-27 03:03:49 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:03:36 | Badalgama (Maha Oya) | 5.73 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 03:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-27 03:03:10 | Giriulla (Maha Oya) | 5.01 | 🟢 Normal | -0.120 |  |
| 2026-10-27 03:03:00 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 03:02:47 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-27 03:02:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:37 | Glencourse (Kelani Ganga) | 14.81 | 🟢 Normal | -0.204 |  |
| 2026-10-27 03:02:18 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-27 03:02:10 | Hanwella (Kelani Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:06 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-27 03:01:51 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 03:01:45 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-10-27 03:01:40 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:01:22 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-27 03:01:11 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 03:00:49 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | -0.020 |  |
| 2026-10-27 02:28:38 | Moragaswewa (Deduru Oya) | 4.90 | 🟡 Alert | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 02:04:30 | Panadugama (Nilwala Ganga) | 6.45 | 🟠 Minor Flood | 0.091 | 🔺 Rising |
| 2026-10-27 02:06:18 | Dunamale (Aththanagalu Oya) | 4.66 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-10-27 03:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 03:04:25 | Rathnapura (Kalu Ganga) | 8.68 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-10-27 02:28:38 | Moragaswewa (Deduru Oya) | 4.90 | 🟡 Alert | 0.055 | 🔺 Rising |
| 2026-10-27 03:04:42 | Baddegama (Gin Ganga) | 3.70 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 03:07:35 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-27 03:01:51 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 03:01:11 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 03:03:36 | Badalgama (Maha Oya) | 5.73 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 02:11:11 | Putupaula (Kalu Ganga) | 3.10 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-10-27 03:00:49 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | -0.020 |  |
| 2026-10-27 03:04:18 | Norwood (Kelani Ganga) | 1.74 | 🟡 Alert | -0.021 |  |
| 2026-10-27 03:06:57 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 03:02:18 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 03:01:40 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:07:24 | Pitabeddara (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:10 | Hanwella (Kelani Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:03:00 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:03:49 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:47 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-27 03:02:06 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-27 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-27 03:01:22 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-10-27 03:03:57 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-10-27 03:07:48 | Moraketiya (Walawe Ganga) | 2.38 | 🟢 Normal | -0.023 |  |
| 2026-10-27 03:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 02:08:38 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.060 |  |
| 2026-10-27 03:01:45 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-10-27 02:04:06 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-10-27 03:08:02 | Holombuwa (Kelani Ganga) | 2.30 | 🟢 Normal | -0.099 |  |
| 2026-10-27 03:03:10 | Giriulla (Maha Oya) | 5.01 | 🟢 Normal | -0.120 |  |
| 2026-10-27 03:05:23 | Peradeniya (Mahaweli Ganga) | 4.24 | 🟢 Normal | -0.151 |  |
| 2026-10-27 03:02:37 | Glencourse (Kelani Ganga) | 14.81 | 🟢 Normal | -0.204 |  |
| 2026-10-27 03:07:52 | Urawa (Nilwala Ganga) | 2.30 | 🟢 Normal | -19.636 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)