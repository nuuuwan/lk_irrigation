# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_17:05:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,226 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 17:05:57 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-10 17:05:43 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 17:05:22 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-10-10 17:05:20 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:05:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.153 |  |
| 2026-10-10 17:05:03 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-10-10 17:04:53 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.079 |  |
| 2026-10-10 17:04:49 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.062 |  |
| 2026-10-10 17:04:44 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 17:04:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 17:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 17:03:44 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.082 |  |
| 2026-10-10 17:03:25 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.062 |  |
| 2026-10-10 17:03:21 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:03:16 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.050 |  |
| 2026-10-10 17:03:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-10-10 17:03:02 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-10-10 17:02:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:02:56 | Moragaswewa (Deduru Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 17:02:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:02:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-10 17:02:34 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 17:02:34 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-10-10 17:02:19 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.100 |  |
| 2026-10-10 17:02:01 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.097 |  |
| 2026-10-10 17:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:01:39 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:01:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:00:40 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:00:38 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.063 |  |
| 2026-10-10 16:31:36 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 17:02:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-10 17:04:44 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 17:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 17:01:39 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 17:04:24 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 17:05:43 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:03 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:56 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:05:20 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:04:18 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:06 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:03:21 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 17:01:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:31:36 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.007 |  |
| 2026-10-10 16:11:08 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-10 16:09:12 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-10-10 17:02:56 | Moragaswewa (Deduru Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 17:02:34 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 17:00:40 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:02:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:02:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-10 17:03:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-10-10 16:06:20 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-10 17:05:22 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-10-10 17:05:57 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-10 17:02:34 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-10-10 17:03:16 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.050 |  |
| 2026-10-10 17:05:03 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.056 |  |
| 2026-10-10 17:04:49 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | -0.062 |  |
| 2026-10-10 17:03:25 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.062 |  |
| 2026-10-10 17:03:02 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-10-10 17:00:38 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.063 |  |
| 2026-10-10 17:04:53 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.079 |  |
| 2026-10-10 17:03:44 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.082 |  |
| 2026-10-10 17:02:01 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.097 |  |
| 2026-10-10 17:02:19 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.100 |  |
| 2026-10-10 17:05:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)