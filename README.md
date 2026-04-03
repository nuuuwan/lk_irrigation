# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_22:18:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,390 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 22:18:59 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:11:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:09:34 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:08:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-04-03 22:08:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-03 22:07:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 22:06:52 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:05:52 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-04-03 22:05:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-04-03 22:05:25 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:05:25 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 22:05:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:04:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:04:24 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:03:50 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-03 22:03:34 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:03:26 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 22:03:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 22:03:06 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 22:03:04 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:02:53 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-04-03 22:02:42 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:02:32 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-03 22:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:02:13 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.011 |  |
| 2026-04-03 22:02:11 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:01:26 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-03 22:01:25 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:01:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:01:20 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 22:01:10 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:01:00 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-03 22:00:50 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:00:39 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 21:48:14 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 22:05:52 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-04-03 22:02:32 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-03 22:01:26 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-03 22:03:50 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-03 22:01:20 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 22:05:25 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 22:01:00 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-03 22:03:06 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 22:03:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 22:03:26 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 22:01:10 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 22:07:52 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 22:00:39 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:18:59 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:01:25 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:06:52 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:09:34 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:03:04 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:01:20 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:02:11 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:11:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:08:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-03 22:04:24 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:04:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:03:34 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-04-03 22:02:13 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.011 |  |
| 2026-04-03 22:08:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-04-03 22:05:39 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-04-03 22:00:50 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:05:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:02:42 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-03 22:02:53 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 21:48:14 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)