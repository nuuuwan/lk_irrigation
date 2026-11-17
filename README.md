# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_04:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 04:03:16 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:50 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:32 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-18 04:02:27 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-18 04:02:23 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:23 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-18 04:02:09 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:29 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:25 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:00 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:00:53 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.032 |  |
| 2026-11-18 03:48:38 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:36:07 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:35:58 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 03:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-11-18 03:04:35 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-11-18 03:02:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-18 01:39:38 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-18 04:02:23 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-18 03:01:31 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 03:02:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 03:03:26 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:00 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:00:53 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:23 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:05:22 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:50 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:02:09 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:22:42 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:05:14 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 02:02:15 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:03:42 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:07:53 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:25 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:03:16 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:48:38 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 02:42:18 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:35:58 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-18 04:01:29 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:03:05 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.005 |  |
| 2026-11-18 03:14:27 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.008 |  |
| 2026-11-18 03:04:40 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-18 04:02:27 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-18 04:02:32 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-11-18 03:02:16 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.011 |  |
| 2026-11-18 03:18:00 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.024 |  |
| 2026-11-18 04:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.032 |  |
| 2026-11-18 03:13:03 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)