# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_10:28:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 10:28:42 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:23:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:14:57 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-11-11 10:12:17 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-11-11 10:11:09 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:10:18 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 10:08:37 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.115 |  |
| 2026-11-11 10:07:41 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-11-11 10:07:39 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -8.090 |  |
| 2026-11-11 10:07:08 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:06:53 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.143 |  |
| 2026-11-11 10:06:37 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.052 |  |
| 2026-11-11 10:06:26 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.028 |  |
| 2026-11-11 10:06:17 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-11-11 10:06:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.094 |  |
| 2026-11-11 10:05:56 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.135 |  |
| 2026-11-11 10:05:49 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:05:35 | Glencourse (Kelani Ganga) | 11.97 | 🟢 Normal | -0.115 |  |
| 2026-11-11 10:04:51 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.063 |  |
| 2026-11-11 10:04:39 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:04:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-11 10:04:25 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-11 10:03:43 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:03:23 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:03:07 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-11-11 10:02:55 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-11-11 10:02:35 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 10:02:21 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 10:02:00 | Moragaswewa (Deduru Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-11-11 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 10:01:25 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 10:01:24 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.124 |  |
| 2026-11-11 10:01:19 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:01:19 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-11-11 10:00:58 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:00:52 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.072 |  |
| 2026-11-11 10:00:30 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:00:14 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -8.090 |  |
| 2026-11-11 09:59:28 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 10:02:35 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 10:10:18 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 10:06:26 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.028 |  |
| 2026-11-11 10:04:51 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.063 |  |
| 2026-11-11 10:02:55 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-11-11 10:01:25 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 10:04:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-11 10:04:25 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-11 09:59:28 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-11 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 10:02:21 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:07:08 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:03:43 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:28:42 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:23:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:00:30 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:03:23 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:05:49 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:11:09 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:14:57 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-11-11 10:07:41 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-11-11 10:04:39 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:01:19 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:00:58 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-11 10:06:17 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-11-11 10:02:00 | Moragaswewa (Deduru Oya) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-11-11 10:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-11-11 10:03:07 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-11-11 10:06:37 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.052 |  |
| 2026-11-11 10:12:17 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-11-11 10:00:52 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.072 |  |
| 2026-11-11 10:06:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.094 |  |
| 2026-11-11 10:05:35 | Glencourse (Kelani Ganga) | 11.97 | 🟢 Normal | -0.115 |  |
| 2026-11-11 10:08:37 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.115 |  |
| 2026-11-11 10:01:24 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.124 |  |
| 2026-11-11 10:05:56 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.135 |  |
| 2026-11-11 10:06:53 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.143 |  |
| 2026-11-11 10:07:39 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -8.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)