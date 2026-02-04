# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_00:56:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,367 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 00:56:39 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:21:30 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-02-05 00:21:09 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-02-05 00:11:41 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:11:36 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-05 00:11:28 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:10:33 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-05 00:09:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-05 00:08:49 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.018 |  |
| 2026-02-05 00:06:29 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:06:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:05:32 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:04:32 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 00:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 00:21:30 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 1.714 | 🔺 Rising |
| 2026-02-05 00:03:09 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 00:04:32 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 00:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-04 23:07:38 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-05 00:10:33 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-05 00:03:08 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-05 00:01:53 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:00:30 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:01:28 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:01:02 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:05:32 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:01:36 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:03:59 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 18:13:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:01:13 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:03:06 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:11:41 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:03:12 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:02:10 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:11:28 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:06:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:06:29 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:56:39 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-04 23:02:16 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 00:11:36 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 00:09:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-05 00:02:29 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.015 |  |
| 2026-02-05 00:08:49 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.018 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-05 00:03:07 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.032 |  |
| 2026-02-05 00:02:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.054 |  |
| 2026-02-04 18:03:35 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)