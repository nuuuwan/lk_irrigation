# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_06:31:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,402 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 06:31:49 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:31:11 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:11:35 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-08-10 06:10:20 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.005 |  |
| 2026-08-10 06:10:03 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 06:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.046 |  |
| 2026-08-10 06:10:00 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 06:08:58 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-08-10 06:08:55 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-08-10 06:08:53 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-08-10 06:08:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:07:55 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-10 06:07:36 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 06:07:00 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:05:25 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-10 06:05:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.155 |  |
| 2026-08-10 06:05:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:05:11 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.056 |  |
| 2026-08-10 06:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:04:34 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.040 | 🔺 Rising |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 06:08:58 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-08-10 06:02:18 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-08-10 06:03:22 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-10 06:04:34 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 06:00:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 06:10:00 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 06:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 06:10:03 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 06:02:25 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 06:07:36 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 06:07:55 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-10 06:01:12 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 06:03:54 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 06:10:20 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.005 |  |
| 2026-08-10 06:03:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:04:21 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:08:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:01:30 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:31:49 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:00:22 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:11 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:05:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:15 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:03:12 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:31:11 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:07 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:11:35 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-08-10 06:02:24 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:01:41 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-10 06:05:25 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-10 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-08-10 06:01:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-08-10 06:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.046 |  |
| 2026-08-10 06:05:11 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.056 |  |
| 2026-08-10 06:05:21 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)