# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_06:04:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 06:04:21 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:54 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 06:03:22 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-10 06:03:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:12 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:11 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:25 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 06:02:24 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:02:18 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-08-10 06:02:15 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:07 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:01:41 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:01:30 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:01:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-08-10 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-08-10 06:01:12 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 06:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 06:00:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 06:00:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:47:12 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-08-10 05:46:54 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:42:17 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-10 05:27:02 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:16:51 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 06:02:18 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-08-10 05:03:43 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-08-10 06:03:22 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-10 03:06:25 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 06:00:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 05:04:22 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 06:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 05:09:58 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-10 06:02:25 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 06:01:12 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 06:03:54 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 05:42:17 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-10 06:03:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:04:21 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:01:29 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:01:30 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:04:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 04:06:43 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:00:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:11 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:05:50 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:15 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:11:15 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:12 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:07 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 05:16:51 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-08-10 06:02:24 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:01:41 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-10 05:05:49 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-10 05:06:36 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-08-10 06:01:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-08-10 05:03:25 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | -0.050 |  |
| 2026-08-10 05:11:11 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.070 |  |
| 2026-08-10 04:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)