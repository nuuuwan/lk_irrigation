# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_19:45:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 19:45:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-11 19:12:42 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-08-11 19:12:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 19:03:14 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-08-11 19:04:09 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-11 19:07:34 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-11 19:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-11 19:06:26 | Peradeniya (Mahaweli Ganga) | 3.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 19:04:38 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-11 19:45:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-11 19:08:51 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:07:00 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:03:50 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:03:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:04:06 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:01:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:12:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:03:22 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:06:08 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:01:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:09:31 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:02:56 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:04:23 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:07:22 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:05:54 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:03:20 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:00:45 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-11 19:12:42 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-08-11 19:07:43 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-08-11 19:07:45 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.009 |  |
| 2026-08-11 19:08:06 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-08-11 19:02:37 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-08-11 18:00:30 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-11 19:02:52 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-08-11 19:03:04 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-11 19:05:32 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-08-11 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.031 |  |
| 2026-08-11 19:05:12 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.034 |  |
| 2026-08-11 19:09:02 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.037 |  |
| 2026-08-11 19:06:13 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)