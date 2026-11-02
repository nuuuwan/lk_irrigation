# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_21:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 21:12:58 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.052 |  |
| 2026-11-02 21:12:40 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.717 | 🔺 Rising |
| 2026-11-02 21:10:51 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-11-02 21:09:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.134 |  |
| 2026-11-02 21:08:25 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:08:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.066 |  |
| 2026-11-02 21:07:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:07:22 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.019 |  |
| 2026-11-02 21:07:16 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-02 21:07:05 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:06:44 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:06:39 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:05:44 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:05:42 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -24.000 |  |
| 2026-11-02 21:05:39 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -24.000 |  |
| 2026-11-02 21:05:23 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 21:05:16 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-02 21:05:11 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-02 21:05:09 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-02 21:05:06 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.045 |  |
| 2026-11-02 21:04:42 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:04:07 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-02 21:03:51 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.037 |  |
| 2026-11-02 21:03:50 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.934 | 🔺 Rising |
| 2026-11-02 21:03:49 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:03:38 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-11-02 21:02:58 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2026-11-02 21:02:45 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-02 21:02:44 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2026-11-02 21:02:15 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.022 |  |
| 2026-11-02 21:02:02 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 21:01:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:01:45 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:01:32 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.512 |  |
| 2026-11-02 21:01:04 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-02 21:00:43 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-02 21:00:10 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 21:03:50 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.934 | 🔺 Rising |
| 2026-11-02 21:10:51 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-11-02 21:03:38 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-11-02 21:12:40 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | 0.717 | 🔺 Rising |
| 2026-11-02 21:07:16 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-02 21:04:07 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-02 21:00:43 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-02 21:05:09 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-02 21:05:11 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 21:02:02 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 21:05:23 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 21:08:25 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:04:42 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:07:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:01:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:00:10 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:07:05 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:03:49 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:01:45 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:06:39 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:06:44 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:05:44 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 21:02:58 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.010 |  |
| 2026-11-02 21:02:45 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-02 21:05:16 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-02 21:07:22 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.019 |  |
| 2026-11-02 21:02:15 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.022 |  |
| 2026-11-02 21:01:04 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 21:03:51 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.037 |  |
| 2026-11-02 21:05:06 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.045 |  |
| 2026-11-02 21:02:44 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2026-11-02 21:12:58 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.052 |  |
| 2026-11-02 21:08:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.066 |  |
| 2026-11-02 21:09:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.134 |  |
| 2026-11-02 21:01:32 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.512 |  |
| 2026-11-02 21:05:42 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)