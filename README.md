# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_05:44:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 05:44:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.082 |  |
| 2026-10-05 05:27:55 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-05 05:11:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-05 05:09:21 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-05 05:06:19 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-05 05:06:10 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.022 |  |
| 2026-10-05 05:06:08 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.170 |  |
| 2026-10-05 05:05:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 05:05:33 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.013 |  |
| 2026-10-05 05:04:35 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 04:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 2.634 | 🔺 Rising |
| 2026-10-05 05:04:08 | Dunamale (Aththanagalu Oya) | 2.73 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-05 05:02:06 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 05:09:21 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-05 05:05:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 05:02:32 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-05 05:03:04 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 05:01:21 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-05 05:06:19 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-05 05:27:55 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-05 05:03:06 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 05:02:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:01:42 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:02:38 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:02:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 05:11:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-05 05:02:42 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 05:02:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-05 05:05:33 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.013 |  |
| 2026-10-05 05:02:37 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-10-05 05:02:06 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.021 |  |
| 2026-10-05 05:01:38 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-05 05:06:10 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.022 |  |
| 2026-10-05 05:02:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.041 |  |
| 2026-10-05 05:02:57 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.046 |  |
| 2026-10-05 05:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.048 |  |
| 2026-10-05 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-10-05 05:01:05 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.060 |  |
| 2026-10-05 05:02:50 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.062 |  |
| 2026-10-05 05:04:35 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.072 |  |
| 2026-10-05 05:44:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.082 |  |
| 2026-10-05 05:02:58 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.136 |  |
| 2026-10-05 05:06:08 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.170 |  |
| 2026-10-05 05:04:14 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.223 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)