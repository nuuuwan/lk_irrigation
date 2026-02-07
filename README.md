# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_23:14:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 23:14:45 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-02-07 23:12:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.009 |  |
| 2026-02-07 23:12:39 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:12:14 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-07 23:11:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.133 |  |
| 2026-02-07 23:09:44 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-02-07 23:09:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.056 |  |
| 2026-02-07 23:08:34 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:08:26 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:06:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:06:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:05:47 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.035 |  |
| 2026-02-07 23:05:19 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:04:19 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-07 23:04:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:56 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.014 |  |
| 2026-02-07 23:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:20 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:11 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:29 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:12 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-02-07 23:02:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:01:26 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 23:01:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:00:53 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:00:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.073 |  |
| 2026-02-07 23:00:10 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:51:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:50:54 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:28:39 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.042 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 23:12:14 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-07 22:28:39 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-07 23:01:26 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 22:00:36 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:08:34 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:05:19 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:00:10 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:12:39 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:50:54 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:04:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:11 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:29 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:06:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:06:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:00:53 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:20 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:03:32 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:02:45 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:51:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:01:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 23:08:26 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 23:14:45 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-02-07 23:12:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.009 |  |
| 2026-02-07 23:09:44 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-02-07 23:04:19 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-07 23:03:56 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.014 |  |
| 2026-02-07 21:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-02-07 23:02:12 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 22:01:33 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.030 |  |
| 2026-02-07 23:05:47 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.035 |  |
| 2026-02-07 23:09:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.056 |  |
| 2026-02-07 23:00:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.073 |  |
| 2026-02-07 23:11:36 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)