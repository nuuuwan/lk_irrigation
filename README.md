# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_07:00:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 07:00:47 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-26 07:00:22 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.010 |  |
| 2026-02-26 06:29:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.001 |  |
| 2026-02-26 06:22:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:21:39 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.008 |  |
| 2026-02-26 06:10:02 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 06:08:59 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:08:45 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:07:50 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-02-26 06:07:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-26 06:07:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:06:12 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:06:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 06:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-02-26 06:04:18 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-26 06:04:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-26 06:04:24 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 06:05:19 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-26 06:07:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-26 06:10:02 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 06:29:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.001 |  |
| 2026-02-26 06:01:08 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:07:28 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:02:33 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:03:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-26 05:05:26 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:03:32 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:02:26 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:01:44 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:04:55 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:03:14 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:01:44 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:06:12 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:08:45 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:22:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:02:19 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-26 06:21:39 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.008 |  |
| 2026-02-26 06:04:52 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 06:04:23 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-26 06:02:17 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-26 07:00:22 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.010 |  |
| 2026-02-26 07:00:47 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-26 06:02:44 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-02-26 06:02:07 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-02-26 06:07:50 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-02-26 06:03:54 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-02-26 06:04:56 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.019 |  |
| 2026-02-26 03:03:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-02-26 06:01:41 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.109 |  |
| 2026-02-26 06:04:03 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)