# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_04:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 04:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -2.880 |  |
| 2026-10-05 04:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -2.880 |  |
| 2026-10-05 04:05:06 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-05 04:04:23 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-10-05 04:04:11 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 04:03:42 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 04:03:34 | Hanwella (Kelani Ganga) | 4.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-05 04:03:25 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:03:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-05 04:03:17 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-05 04:02:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-10-05 04:02:41 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:02:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:02:19 | Glencourse (Kelani Ganga) | 12.34 | 🟢 Normal | -306.000 |  |
| 2026-10-05 04:02:17 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -306.000 |  |
| 2026-10-05 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 04:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 04:01:35 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -59.016 |  |
| 2026-10-05 04:01:35 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-05 04:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-10-05 04:01:19 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | -0.184 |  |
| 2026-10-05 04:01:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-10-05 04:01:09 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-05 04:00:57 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-05 04:00:28 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-05 03:55:29 | Horowpothana (Yan Oya) | 7.71 | 🟠 Minor Flood | -59.016 |  |
| 2026-10-05 03:47:27 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 03:10:39 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-05 04:03:17 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-05 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 03:01:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 03:03:30 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-05 04:04:11 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 01:09:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 03:07:29 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 04:03:42 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 04:03:34 | Hanwella (Kelani Ganga) | 4.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-05 04:02:41 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:02:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:03:25 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 04:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:02:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 04:00:57 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-05 03:03:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 04:01:35 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 04:05:06 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-05 04:00:28 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-05 04:02:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-10-05 04:01:09 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-05 04:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-10-05 03:19:10 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.024 |  |
| 2026-10-05 04:03:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-05 04:04:23 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-10-05 04:01:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-10-05 03:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.056 |  |
| 2026-10-05 03:06:06 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-10-05 03:05:53 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.169 |  |
| 2026-10-05 04:01:19 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | -0.184 |  |
| 2026-10-05 03:11:04 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.900 |  |
| 2026-10-05 04:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -2.880 |  |
| 2026-10-05 04:01:35 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -59.016 |  |
| 2026-10-05 04:02:19 | Glencourse (Kelani Ganga) | 12.34 | 🟢 Normal | -306.000 |  |
| 2026-10-05 03:04:28 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)