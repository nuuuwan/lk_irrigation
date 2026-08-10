# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_08:27:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 08:27:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:13:37 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-10 08:13:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.107 |  |
| 2026-08-10 08:13:08 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:13:03 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:12:03 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 08:11:16 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-08-10 08:10:49 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 08:08:40 | Peradeniya (Mahaweli Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-08-10 08:08:11 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-10 08:07:40 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.059 |  |
| 2026-08-10 08:07:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 08:08:11 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-10 08:00:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-10 08:00:44 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 08:03:15 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 08:04:42 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 08:13:37 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-10 08:01:37 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 08:00:31 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 08:10:49 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 08:12:03 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 08:02:14 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:27:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:04:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:02:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:13:08 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:01:24 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:05:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:13:03 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:03:51 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:03:49 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:05:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:00:56 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:07:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:03:44 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 08:05:14 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-08-10 08:07:25 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-10 08:05:40 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-10 08:04:05 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.010 |  |
| 2026-08-10 08:03:39 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-10 08:05:38 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-08-10 08:08:40 | Peradeniya (Mahaweli Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-08-10 08:11:16 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-08-10 08:02:12 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-08-10 08:07:40 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.059 |  |
| 2026-08-10 08:04:58 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.079 |  |
| 2026-08-10 08:01:27 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.096 |  |
| 2026-08-10 08:13:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.107 |  |
| 2026-08-10 08:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.114 |  |
| 2026-08-10 08:03:29 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)