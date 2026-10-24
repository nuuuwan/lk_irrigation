# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_07:13:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 07:13:18 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:13:13 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.017 |  |
| 2026-10-24 07:13:05 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:11:09 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:10:55 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 07:09:26 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.086 |  |
| 2026-10-24 07:09:04 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-10-24 07:08:38 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-24 07:06:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:06:04 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.015 |  |
| 2026-10-24 07:05:40 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.028 |  |
| 2026-10-24 07:05:29 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-24 07:05:23 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:04:51 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 07:04:42 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.029 |  |
| 2026-10-24 07:04:25 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.061 |  |
| 2026-10-24 07:04:23 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.166 |  |
| 2026-10-24 07:04:18 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-10-24 07:04:14 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-24 07:04:09 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 07:03:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-24 07:03:26 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-10-24 07:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.110 |  |
| 2026-10-24 07:02:39 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-10-24 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.138 |  |
| 2026-10-24 07:02:21 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-10-24 07:02:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.129 |  |
| 2026-10-24 07:02:11 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-10-24 07:01:56 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-24 07:01:49 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:01:37 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-24 07:01:01 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.096 |  |
| 2026-10-24 07:00:23 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-10-24 07:00:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.155 |  |
| 2026-10-24 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-24 06:33:40 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 07:08:38 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-24 07:05:29 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-24 07:01:37 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-24 06:00:12 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-24 07:04:14 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-24 07:04:51 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 07:04:09 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 07:10:55 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 07:01:49 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:13:05 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:11:09 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:06:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:13:18 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:05:23 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 07:09:04 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-10-24 07:03:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-24 07:01:56 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-24 07:00:23 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-10-24 07:06:04 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.015 |  |
| 2026-10-24 07:13:13 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.017 |  |
| 2026-10-24 07:02:21 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-10-24 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 07:04:18 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-10-24 06:04:54 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | -0.028 |  |
| 2026-10-24 07:05:40 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.028 |  |
| 2026-10-24 07:04:42 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.029 |  |
| 2026-10-24 07:03:26 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-10-24 07:02:39 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-10-24 07:02:11 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-10-24 07:04:25 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.061 |  |
| 2026-10-24 07:09:26 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.086 |  |
| 2026-10-24 07:01:01 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.096 |  |
| 2026-10-24 07:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.110 |  |
| 2026-10-24 07:02:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.129 |  |
| 2026-10-24 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.138 |  |
| 2026-10-24 07:00:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.155 |  |
| 2026-10-24 07:04:23 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.166 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)