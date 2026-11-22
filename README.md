# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_21:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 21:03:15 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:52 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:39 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.012 |  |
| 2026-11-22 21:02:13 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:02:11 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:06 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-22 21:01:39 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:01:38 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-22 21:01:25 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | -0.154 |  |
| 2026-11-22 21:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:01:23 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:01:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-11-22 21:00:59 | Moraketiya (Walawe Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:00:11 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 20:25:08 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 20:04:03 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-11-22 20:04:00 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-22 20:06:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 20:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-22 21:01:38 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-22 21:00:11 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 20:01:53 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 21:01:23 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:01:39 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:03:15 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:52 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:03:54 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:06:41 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:13 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:25:08 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.007 |  |
| 2026-11-22 20:15:21 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.008 |  |
| 2026-11-22 20:15:14 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.008 |  |
| 2026-11-22 21:02:06 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-22 21:01:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-11-22 20:01:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-11-22 21:02:39 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.012 |  |
| 2026-11-22 21:02:11 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-11-22 20:07:53 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:00:59 | Moraketiya (Walawe Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-22 21:02:13 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 20:09:21 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-11-22 20:04:23 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.049 |  |
| 2026-11-22 20:02:24 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.050 |  |
| 2026-11-22 20:03:52 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.051 |  |
| 2026-11-22 20:13:57 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.062 |  |
| 2026-11-22 20:00:45 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.105 |  |
| 2026-11-22 21:01:25 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | -0.154 |  |
| 2026-11-22 20:07:52 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)