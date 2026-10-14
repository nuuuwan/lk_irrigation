# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_21:09:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,981 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 21:09:11 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:08:49 | Holombuwa (Kelani Ganga) | 4.80 | 🟠 Minor Flood | -0.204 |  |
| 2026-10-14 21:08:22 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:07:56 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 21:07:37 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:07:26 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:07:03 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-10-14 21:06:56 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.088 |  |
| 2026-10-14 21:06:46 | Rathnapura (Kalu Ganga) | 5.27 | 🟡 Alert | 0.508 | 🔺 Rising |
| 2026-10-14 21:06:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-10-14 21:06:09 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-14 21:05:32 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-14 21:05:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-14 21:05:14 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-14 21:05:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:05:11 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 21:04:23 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.285 |  |
| 2026-10-14 21:04:18 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-14 21:04:18 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-10-14 21:04:15 | Peradeniya (Mahaweli Ganga) | 4.14 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-14 21:04:06 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-10-14 21:03:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:05 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:02 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 21:02:45 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 21:02:43 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.125 |  |
| 2026-10-14 21:02:40 | Yaka Wewa (Ma Oya) | 1.43 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-10-14 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-14 21:02:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:02:05 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:01:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:00:49 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:00:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 21:07:56 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 21:08:49 | Holombuwa (Kelani Ganga) | 4.80 | 🟠 Minor Flood | -0.204 |  |
| 2026-10-14 21:06:46 | Rathnapura (Kalu Ganga) | 5.27 | 🟡 Alert | 0.508 | 🔺 Rising |
| 2026-10-14 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-14 20:10:05 | Panadugama (Nilwala Ganga) | 5.49 | 🟡 Alert | -0.051 |  |
| 2026-10-14 21:06:56 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.088 |  |
| 2026-10-14 21:04:18 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-10-14 21:02:40 | Yaka Wewa (Ma Oya) | 1.43 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-10-14 21:04:18 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-14 21:05:32 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-14 21:05:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-14 21:05:14 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-14 21:04:15 | Peradeniya (Mahaweli Ganga) | 4.14 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-14 21:05:11 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 21:06:09 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-14 21:02:45 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 21:03:02 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:00:49 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:02:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:09:11 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:05 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:00:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:01:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:02:05 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:08:22 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:07:26 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 21:05:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-14 20:02:38 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-14 21:07:03 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-10-14 21:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-10-14 21:06:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-10-14 21:02:43 | Thawalama (Gin Ganga) | 3.17 | 🟢 Normal | -0.125 |  |
| 2026-10-14 21:04:23 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.285 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)