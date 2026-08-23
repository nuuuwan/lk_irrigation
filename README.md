# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_05:53:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 05:53:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.056 |  |
| 2026-08-23 05:37:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:37:50 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:37:26 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:31:34 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -18.000 |  |
| 2026-08-23 05:31:32 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -18.000 |  |
| 2026-08-23 05:14:16 | Norwood (Kelani Ganga) | 0.06 | 🟢 Normal | -77.250 |  |
| 2026-08-23 05:13:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:13:52 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -77.250 |  |
| 2026-08-23 05:11:40 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-08-23 05:10:27 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-08-23 05:09:19 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.005 |  |
| 2026-08-23 05:09:14 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.243 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 05:09:14 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-08-23 04:01:54 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-23 05:03:21 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-23 05:03:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-23 05:01:52 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-23 05:01:57 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-23 05:37:26 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:01:17 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:00:40 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:02:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:01:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:02:22 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:37:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:04:55 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:04:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:02:36 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:13:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:02:55 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:06:24 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:03:42 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:01:29 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 05:09:19 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.005 |  |
| 2026-08-23 05:10:27 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-08-23 05:02:26 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-23 05:05:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-08-23 05:02:32 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.016 |  |
| 2026-08-23 05:11:40 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-08-23 05:05:11 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-08-23 05:05:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-08-23 05:01:48 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.052 |  |
| 2026-08-23 05:53:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.056 |  |
| 2026-08-23 05:05:36 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-08-23 05:04:10 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.160 |  |
| 2026-08-23 05:31:34 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -18.000 |  |
| 2026-08-23 05:14:16 | Norwood (Kelani Ganga) | 0.06 | 🟢 Normal | -77.250 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)