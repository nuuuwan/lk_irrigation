# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_05:10:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,540 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 05:10:02 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:10:00 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-14 05:08:23 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:06:27 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 05:05:31 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:05:09 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:04:46 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 05:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-02-14 05:04:14 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:04:13 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-02-14 05:03:29 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-02-14 05:03:24 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-14 05:02:55 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-14 05:02:53 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 05:02:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:29 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-02-14 05:02:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:09 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -4.320 |  |
| 2026-02-14 05:02:07 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:02:00 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:57 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.201 |  |
| 2026-02-14 05:01:45 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-14 05:01:45 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:40 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:28 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:00:58 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-02-14 05:00:18 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:00:04 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -4.320 |  |
| 2026-02-14 04:30:37 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:21:42 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:21:20 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 05:02:56 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-14 04:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-14 05:01:45 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-14 05:02:53 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:09:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 05:06:27 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:01:55 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 05:04:46 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 05:02:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:40 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:05:31 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:30:37 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:10:02 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:03:24 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:45 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:05:09 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:01:28 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 05:02:42 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:07:33 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-02-14 05:04:14 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:06:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:08:23 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:02:07 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-14 05:00:18 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:08:19 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-14 05:04:13 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-02-14 05:10:00 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-14 05:03:29 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-02-14 05:00:58 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-02-14 05:02:29 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-02-14 05:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-14 05:01:57 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.201 |  |
| 2026-02-14 05:02:09 | Kithulgala (Kelani Ganga) | 1.05 | 🟢 Normal | -4.320 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)