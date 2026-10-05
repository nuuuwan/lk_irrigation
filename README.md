# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_04:05:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 04:05:53 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:05:33 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.029 |  |
| 2026-10-06 04:05:05 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.042 |  |
| 2026-10-06 04:05:03 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 04:04:54 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:04:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:03:44 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 04:03:17 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.060 |  |
| 2026-10-06 04:03:06 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 04:02:48 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-06 04:02:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:02:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2026-10-06 04:02:23 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.214 |  |
| 2026-10-06 04:02:15 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 04:02:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-06 04:02:11 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-10-06 04:02:08 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-06 04:01:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:01:07 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 04:01:02 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.124 |  |
| 2026-10-06 04:00:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-10-06 04:00:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 04:00:14 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.050 |  |
| 2026-10-06 03:50:32 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-06 03:48:02 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 03:06:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-06 03:50:32 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-06 03:04:15 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-06 04:05:03 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-06 04:02:12 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-06 04:03:06 | Hanwella (Kelani Ganga) | 4.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-06 04:02:15 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 04:01:07 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 04:03:44 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 03:21:46 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-06 04:00:15 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 04:01:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:00:33 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:02:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:05:53 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-06 04:04:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:10:14 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-10-06 03:48:02 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.007 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-06 04:02:48 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-06 03:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-10-06 04:00:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-10-06 01:03:14 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-10-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-10-06 04:05:33 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.029 |  |
| 2026-10-06 04:02:08 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-10-06 04:05:05 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.042 |  |
| 2026-10-06 02:13:23 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-06 04:00:14 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.050 |  |
| 2026-10-06 04:02:11 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-10-06 03:12:00 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.056 |  |
| 2026-10-06 04:03:17 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.060 |  |
| 2026-10-06 04:02:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2026-10-06 04:01:02 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.124 |  |
| 2026-10-06 04:02:23 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)