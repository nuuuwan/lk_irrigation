# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_02:07:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 02:07:38 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-24 02:07:04 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -8.182 |  |
| 2026-10-24 02:06:42 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | -8.182 |  |
| 2026-10-24 02:06:20 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.087 |  |
| 2026-10-24 02:05:07 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-24 02:05:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:03:50 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.015 |  |
| 2026-10-24 02:03:48 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-10-24 02:03:47 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-24 02:03:46 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-24 02:03:28 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -108.000 |  |
| 2026-10-24 02:03:26 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -108.000 |  |
| 2026-10-24 02:03:25 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-24 02:03:25 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:03:01 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.050 |  |
| 2026-10-24 02:02:53 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:02:44 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-24 02:02:40 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:02:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:02:09 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 02:01:51 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-24 02:01:43 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.090 |  |
| 2026-10-24 02:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-10-24 02:01:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-24 02:01:16 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 02:01:07 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-10-24 02:01:02 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 02:00:15 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 02:05:07 | Glencourse (Kelani Ganga) | 11.44 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-24 02:07:38 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-24 02:03:47 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-24 02:01:02 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 02:02:09 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 02:01:16 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 02:00:15 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:02:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-24 00:11:13 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:03:25 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:05:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:04:05 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:02:53 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-24 01:06:33 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-24 02:03:46 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-24 02:01:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 00:03:58 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 02:03:48 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-10-24 02:01:07 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-10-24 02:03:50 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.015 |  |
| 2026-10-24 01:09:47 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | -0.019 |  |
| 2026-10-24 02:03:25 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-24 02:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-10-24 02:02:44 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:05:15 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-10-24 01:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.028 |  |
| 2026-10-24 02:01:51 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-24 01:03:54 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 02:03:01 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.050 |  |
| 2026-10-24 01:01:48 | Moragaswewa (Deduru Oya) | 3.89 | 🟢 Normal | -0.070 |  |
| 2026-10-24 02:06:20 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.087 |  |
| 2026-10-24 02:01:43 | Ellagawa (Kalu Ganga) | 6.83 | 🟢 Normal | -0.090 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |
| 2026-10-24 02:07:04 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -8.182 |  |
| 2026-10-24 02:03:28 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)