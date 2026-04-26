# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_04:37:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 04:37:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:12:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-04-27 04:10:49 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 04:10:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-04-27 04:09:30 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.333 |  |
| 2026-04-27 04:08:49 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-27 04:08:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-04-27 04:08:07 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 04:07:42 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.333 |  |
| 2026-04-27 04:07:05 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.333 |  |
| 2026-04-27 04:06:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -36.000 |  |
| 2026-04-27 04:06:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -36.000 |  |
| 2026-04-27 04:06:45 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-04-27 04:06:13 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-27 04:05:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 04:05:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-04-27 04:04:57 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:04:24 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-27 04:03:59 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 04:03:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-04-27 04:03:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:03:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-27 04:03:10 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-27 04:03:01 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 04:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-04-27 04:02:47 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:02:40 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:02:13 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-04-27 04:02:11 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 04:01:56 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-04-27 04:01:47 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 04:01:35 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.063 |  |
| 2026-04-27 04:01:15 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-04-27 04:00:19 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:00:17 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 04:05:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-04-27 04:03:10 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-27 04:04:24 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-27 04:10:49 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-27 04:08:49 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-27 04:06:13 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-27 04:03:59 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-27 04:03:01 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 03:20:31 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-27 04:02:11 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 04:01:47 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 04:05:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 04:02:47 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:00:19 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:03:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:37:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:02:40 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:01:35 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 03:06:39 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:04:57 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 04:06:45 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-04-27 04:01:56 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-04-27 04:10:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-04-27 04:12:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-27 04:01:15 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-04-27 04:08:07 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:00:14 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-27 04:08:26 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-04-27 04:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-04-27 04:02:13 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-27 04:03:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-04-27 04:03:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-27 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.063 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-27 04:09:30 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.333 |  |
| 2026-04-27 04:06:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)