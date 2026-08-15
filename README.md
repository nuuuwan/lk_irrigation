# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_14:16:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 14:16:35 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-15 14:10:41 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-08-15 14:07:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:06:33 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.133 |  |
| 2026-08-15 14:06:23 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:06:13 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-08-15 14:05:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:05:12 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 14:04:42 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.020 |  |
| 2026-08-15 14:04:29 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 14:01:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-15 14:01:36 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-15 14:16:35 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-15 14:05:12 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 14:02:55 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.005 |  |
| 2026-08-15 14:01:02 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:02:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:01:59 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:02:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:00:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:02:29 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:05:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:03:29 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:07:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:04:29 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:03:14 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:03:21 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:03:03 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:06:23 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:02:23 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:04:11 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:01:27 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:01:23 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 14:03:43 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-08-15 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-08-15 14:03:49 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-15 14:02:17 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-15 14:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-08-15 14:02:47 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-08-15 14:04:42 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.020 |  |
| 2026-08-15 14:10:41 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-08-15 14:02:19 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.022 |  |
| 2026-08-15 14:04:15 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-08-15 14:01:03 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-08-15 14:03:28 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-08-15 14:06:13 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-08-15 14:03:27 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.041 |  |
| 2026-08-15 14:00:25 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.091 |  |
| 2026-08-15 14:06:33 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)