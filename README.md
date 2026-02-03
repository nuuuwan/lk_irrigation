# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_15:25:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 15:25:24 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:22:46 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:09:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:09:09 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.057 |  |
| 2026-02-03 15:08:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:07:26 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:06:41 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:05:29 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:05:19 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-02-03 15:05:17 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 15:04:25 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:04:23 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:04:20 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.059 |  |
| 2026-02-03 15:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-03 15:03:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:44 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-02-03 15:03:14 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:08 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:02:51 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 15:02:41 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:02:30 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.039 |  |
| 2026-02-03 15:02:11 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:01:21 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:00:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-02-03 15:00:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 15:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 15:02:51 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 15:05:17 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 15:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:00:09 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:02:11 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:06:41 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:05:29 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:00:09 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:04:25 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:14 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:08:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:09:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:25:24 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:07:26 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 15:03:44 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 15:02:41 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:01:21 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:03:08 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:00:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-03 15:03:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-03 15:05:19 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-02-03 15:02:30 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.039 |  |
| 2026-02-03 15:09:09 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.057 |  |
| 2026-02-03 15:04:20 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.059 |  |
| 2026-02-03 06:04:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.064 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 15:00:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-02-03 06:01:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)