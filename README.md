# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_05:07:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 05:07:23 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.068 |  |
| 2026-10-12 05:07:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.028 |  |
| 2026-10-12 05:05:22 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-10-12 05:04:42 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.035 |  |
| 2026-10-12 05:03:56 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-12 05:03:49 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:03:45 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.070 |  |
| 2026-10-12 05:03:39 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:03:37 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-12 05:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-12 05:02:49 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 05:02:34 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.129 |  |
| 2026-10-12 05:02:32 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:02:09 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 05:02:07 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-10-12 05:02:05 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.032 |  |
| 2026-10-12 05:01:57 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.067 |  |
| 2026-10-12 05:01:44 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.117 |  |
| 2026-10-12 05:01:29 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 05:01:15 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-12 05:01:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-12 05:00:22 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-10-12 05:00:09 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:59:40 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-12 04:43:23 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-12 04:34:42 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:30:04 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:28:52 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-10-12 04:23:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.841 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 04:23:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.841 | 🔺 Rising |
| 2026-10-12 05:03:37 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-12 04:02:51 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 05:03:56 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-12 04:01:06 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-12 04:07:06 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-12 05:01:29 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 05:02:09 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 05:02:49 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 05:03:39 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 02:04:14 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:06:39 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:02:32 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:03:49 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:10:07 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 03:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 05:00:09 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 04:01:46 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 05:01:57 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 05:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-12 04:59:40 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-12 05:02:07 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-10-12 05:01:15 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-12 05:01:14 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-12 05:07:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.028 |  |
| 2026-10-12 04:11:15 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-10-12 05:02:05 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.032 |  |
| 2026-10-12 05:04:42 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.035 |  |
| 2026-10-12 05:00:22 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-10-12 05:05:22 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-10-12 05:01:48 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.067 |  |
| 2026-10-12 05:07:23 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.068 |  |
| 2026-10-12 05:03:45 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.070 |  |
| 2026-10-12 05:01:44 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.117 |  |
| 2026-10-12 05:02:34 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | -0.129 |  |
| 2026-10-12 04:09:26 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)