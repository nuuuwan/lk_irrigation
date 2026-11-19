# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_13:03:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 13:03:29 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:11 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:50 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:41 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 13:02:32 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:26 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:12 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:11 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:53 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:34 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:19 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 13:01:14 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:28 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:04 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-19 12:02:31 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 13:01:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 13:00:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:50 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:26 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:02:32 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:06:24 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:05:39 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:00:28 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:02:00 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:53 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:07:41 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:02:22 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:23 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:02:07 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:02:14 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 12:05:47 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:01:19 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 13:03:15 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:29 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-19 12:04:04 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.010 |  |
| 2026-11-19 12:05:45 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:03:11 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:11 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:12 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:14 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:01:34 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:00:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 13:02:41 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:01:02 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:00:56 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:01:08 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:03:00 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:03:05 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.011 |  |
| 2026-11-19 12:02:54 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)