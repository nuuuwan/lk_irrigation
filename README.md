# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_04:38:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 04:38:25 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:27:28 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:15:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-04 04:08:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 04:08:06 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-04 04:08:05 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-04 04:07:31 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-04 04:06:59 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-02-04 04:06:56 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 04:06:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-04 04:05:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:05:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-04 04:04:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:04:28 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:04:11 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.194 |  |
| 2026-02-04 04:04:06 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 04:03:47 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:42 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:27 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:10 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-02-04 04:03:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-02-04 04:02:40 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:02:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-04 04:02:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-04 04:01:00 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 04:08:06 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 04:07:31 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-04 04:15:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-04 04:05:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-04 04:06:00 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-04 04:06:56 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 04:02:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-04 04:08:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 04:04:06 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 04:05:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:01:00 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:04:28 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:27 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:38:25 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:02:40 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 03:50:17 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:47 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:04:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:27:28 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:03:42 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 04:06:59 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 04:03:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-02-04 03:03:19 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-04 04:02:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-04 03:15:34 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.012 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-04 04:03:10 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-02-03 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.068 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-04 01:04:18 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.074 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-04 04:04:11 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)