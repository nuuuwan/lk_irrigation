# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_20:08:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,761 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 20:08:27 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-16 20:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -0.009 |  |
| 2026-10-16 20:07:23 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-16 20:06:59 | Moragaswewa (Deduru Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-16 20:06:49 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:06:25 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:05:40 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-10-16 20:05:09 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:05:01 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-16 20:04:58 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.141 |  |
| 2026-10-16 20:04:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-10-16 20:04:49 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-10-16 20:04:45 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 20:04:37 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 20:04:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:03:50 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-16 20:03:28 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:03:26 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.158 |  |
| 2026-10-16 20:03:23 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-16 20:02:56 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:02:34 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-16 20:02:20 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-16 20:02:15 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 1.084 | 🔺 Rising |
| 2026-10-16 20:02:12 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:02:09 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:01:47 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:01:37 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-16 20:01:30 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 20:01:27 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-16 20:00:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-10-16 20:00:12 | Wellawaya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-10-16 19:35:20 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 19:16:14 | Panadugama (Nilwala Ganga) | 6.41 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-16 20:07:23 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-16 20:03:50 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-16 20:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -0.009 |  |
| 2026-10-16 20:02:15 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 1.084 | 🔺 Rising |
| 2026-10-16 20:05:40 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-10-16 20:04:49 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-10-16 20:00:12 | Wellawaya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-10-16 20:02:20 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-16 19:20:39 | Urawa (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-10-16 20:03:23 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-16 20:01:27 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-16 20:05:01 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-16 20:08:27 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-16 20:01:37 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-16 20:04:45 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 19:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-16 20:01:30 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 19:11:07 | Pitabeddara (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-16 20:04:37 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 20:02:12 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:06:49 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:02:09 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 20:03:28 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 19:09:44 | Ellagawa (Kalu Ganga) | 7.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 20:06:25 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:01:47 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:02:56 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:05:09 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:04:29 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 20:04:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 20:06:59 | Moragaswewa (Deduru Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-16 20:02:34 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-16 20:00:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-10-16 20:04:58 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.141 |  |
| 2026-10-16 20:03:26 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)