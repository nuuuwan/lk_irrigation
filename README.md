# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_09:18:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 09:18:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:09:57 | Rathnapura (Kalu Ganga) | 8.55 | 🟠 Minor Flood | -0.045 |  |
| 2026-10-27 09:09:21 | Dunamale (Aththanagalu Oya) | 4.81 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-10-27 09:08:54 | Baddegama (Gin Ganga) | 3.93 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-27 09:08:11 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.062 |  |
| 2026-10-27 09:06:58 | Holombuwa (Kelani Ganga) | 1.85 | 🟢 Normal | -0.051 |  |
| 2026-10-27 09:06:33 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | -0.203 |  |
| 2026-10-27 09:05:14 | Badalgama (Maha Oya) | 5.44 | 🟡 Alert | -0.109 |  |
| 2026-10-27 09:05:09 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-27 09:04:53 | Hanwella (Kelani Ganga) | 6.47 | 🟢 Normal | -0.088 |  |
| 2026-10-27 09:04:34 | Putupaula (Kalu Ganga) | 3.25 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 09:04:28 | Giriulla (Maha Oya) | 3.93 | 🟢 Normal | -0.188 |  |
| 2026-10-27 09:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2026-10-27 09:04:15 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 09:04:09 | Magura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.019 |  |
| 2026-10-27 09:04:07 | Panadugama (Nilwala Ganga) | 6.43 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-27 09:03:40 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | -0.041 |  |
| 2026-10-27 09:03:24 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 09:03:13 | Pitabeddara (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.171 |  |
| 2026-10-27 09:02:57 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-27 09:02:56 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-10-27 09:02:54 | Ellagawa (Kalu Ganga) | 9.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 09:02:53 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:02:50 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -98.809 |  |
| 2026-10-27 09:02:40 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:02:31 | Thawalama (Gin Ganga) | 4.44 | 🟡 Alert | -0.278 |  |
| 2026-10-27 09:02:26 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-27 09:02:15 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-27 09:02:04 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.050 |  |
| 2026-10-27 09:02:03 | Thaldena (Mahaweli Ganga) | 1.82 | 🟢 Normal | -98.809 |  |
| 2026-10-27 09:02:02 | Galgamuwa (Mee Oya) | 4.08 | 🟢 Normal | -0.022 |  |
| 2026-10-27 09:01:50 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:01:41 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.109 |  |
| 2026-10-27 09:01:28 | Nagalagam Street (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-27 09:01:24 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.022 |  |
| 2026-10-27 09:01:19 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:01:18 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-10-27 09:00:47 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:00:44 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-10-27 09:00:16 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 09:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2026-10-27 09:09:21 | Dunamale (Aththanagalu Oya) | 4.81 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-10-27 09:04:07 | Panadugama (Nilwala Ganga) | 6.43 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-27 09:09:57 | Rathnapura (Kalu Ganga) | 8.55 | 🟠 Minor Flood | -0.045 |  |
| 2026-10-27 09:08:54 | Baddegama (Gin Ganga) | 3.93 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-27 09:04:34 | Putupaula (Kalu Ganga) | 3.25 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 09:01:18 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-10-27 09:04:15 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 09:04:09 | Magura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.019 |  |
| 2026-10-27 09:05:14 | Badalgama (Maha Oya) | 5.44 | 🟡 Alert | -0.109 |  |
| 2026-10-27 09:02:31 | Thawalama (Gin Ganga) | 4.44 | 🟡 Alert | -0.278 |  |
| 2026-10-27 09:05:09 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-27 09:02:57 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-27 09:02:54 | Ellagawa (Kalu Ganga) | 9.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 09:03:24 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 09:01:50 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:00:47 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:18:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:02:40 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:02:53 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:02:15 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-27 09:00:16 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-27 09:00:44 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-10-27 09:02:56 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-10-27 09:02:26 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-27 09:01:24 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.022 |  |
| 2026-10-27 09:02:02 | Galgamuwa (Mee Oya) | 4.08 | 🟢 Normal | -0.022 |  |
| 2026-10-27 09:01:28 | Nagalagam Street (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-27 08:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-10-27 09:03:40 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | -0.041 |  |
| 2026-10-27 09:02:04 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.050 |  |
| 2026-10-27 09:06:58 | Holombuwa (Kelani Ganga) | 1.85 | 🟢 Normal | -0.051 |  |
| 2026-10-27 09:08:11 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.062 |  |
| 2026-10-27 09:04:53 | Hanwella (Kelani Ganga) | 6.47 | 🟢 Normal | -0.088 |  |
| 2026-10-27 09:01:41 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.109 |  |
| 2026-10-27 09:03:13 | Pitabeddara (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.171 |  |
| 2026-10-27 09:04:28 | Giriulla (Maha Oya) | 3.93 | 🟢 Normal | -0.188 |  |
| 2026-10-27 09:06:33 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | -0.203 |  |
| 2026-10-27 09:02:50 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -98.809 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)