# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_04:30:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 04:30:37 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:21:42 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-14 04:21:20 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 04:09:52 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.248 |  |
| 2026-02-14 04:09:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:08:19 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:06:41 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:06:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:06:24 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:05:59 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 04:05:52 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-14 04:05:18 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:05:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:05:02 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.248 |  |
| 2026-02-14 04:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-14 04:03:28 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:03:23 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:03:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:02:56 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:02:46 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-02-14 04:02:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.203 |  |
| 2026-02-14 04:02:05 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:55 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:01:40 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:32 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:01:10 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:00:54 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.030 |  |
| 2026-02-14 04:00:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 04:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-14 04:21:20 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 04:05:52 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-14 04:05:59 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 04:00:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:09:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:01:55 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:03:28 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 04:21:42 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-14 04:01:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:40 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:34 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:30:37 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:20 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:03:23 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:06:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:05:18 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:02:05 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:19:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:03:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:01:10 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 04:05:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:07:33 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-02-14 03:06:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:06:24 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:01:32 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-14 04:06:41 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:02:56 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:08:19 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-14 04:00:54 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.030 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-14 04:02:46 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-02-14 04:02:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.203 |  |
| 2026-02-14 03:03:16 | Giriulla (Maha Oya) | 0.50 | 🟢 Normal | -0.211 |  |
| 2026-02-14 04:09:52 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.248 |  |
| 2026-02-14 03:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.348 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)