# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_03:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,052 measurements** from **39** stations.
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
| 2026-09-06 03:02:56 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-09-06 03:02:48 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:29 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:18 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-09-06 03:02:03 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:02 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:01:58 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -1.500 |  |
| 2026-09-06 03:01:55 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-09-06 03:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:01:28 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-09-06 03:01:14 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:00:57 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:00:54 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:59:10 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -1.500 |  |
| 2026-09-06 02:37:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 3.789 | 🔺 Rising |
| 2026-09-06 02:36:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 3.789 | 🔺 Rising |
| 2026-09-06 02:18:32 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 02:37:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 3.789 | 🔺 Rising |
| 2026-09-06 03:01:55 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-09-06 02:06:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-06 02:06:10 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-06 03:02:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:00:57 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:03 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:01:41 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:05:48 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:56 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:18 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:36 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:00:15 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:48 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:03:06 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:29 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-05 18:13:48 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:01:49 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-06 02:18:32 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:01:14 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 03:02:02 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 01:59:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.006 |  |
| 2026-09-06 02:03:24 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-06 03:02:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-09-06 01:01:55 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-09-06 02:08:52 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.018 |  |
| 2026-09-06 02:09:47 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-09-06 02:05:25 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-06 02:05:47 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.022 |  |
| 2026-09-06 03:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-09-06 03:01:28 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-09-06 02:02:22 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.046 |  |
| 2026-09-05 18:09:31 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.049 |  |
| 2026-09-06 02:02:12 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.073 |  |
| 2026-09-06 01:06:35 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.234 |  |
| 2026-09-06 03:01:58 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)