# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_11:33:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 11:33:15 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-24 11:13:56 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-06-24 11:11:08 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:10:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:10:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:10:11 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.070 |  |
| 2026-06-24 11:01:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-24 11:01:30 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 11:01:28 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 11:02:32 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 11:02:22 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 11:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 11:01:37 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 11:05:52 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-24 11:33:15 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-24 11:01:37 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:03:47 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:01:09 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:04:14 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:04:20 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:02:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:03:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:03:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:10:44 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:06:26 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:01:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:11:08 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:10:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 11:06:56 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-06-24 11:04:24 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-06-24 11:01:09 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-24 11:01:37 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-06-24 11:08:35 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-06-24 11:00:14 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.020 |  |
| 2026-06-24 11:13:56 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-06-24 11:08:14 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-06-24 11:01:04 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.032 |  |
| 2026-06-24 11:10:11 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.036 |  |
| 2026-06-24 11:06:49 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.036 |  |
| 2026-06-24 11:02:56 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.061 |  |
| 2026-06-24 11:03:21 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.069 |  |
| 2026-06-24 11:02:01 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.119 |  |
| 2026-06-24 11:05:51 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)