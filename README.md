# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_19:00:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,064 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 19:00:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 19:00:22 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:00:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 18:15:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:07:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:07:49 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:06:07 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:14 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:05:02 | Padiyathalawa (Maduru Oya) | 2.67 | 🟢 Normal | -0.421 |  |
| 2026-02-14 18:04:30 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 18:04:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-02-14 19:00:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 18:02:58 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-14 19:00:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-14 18:02:18 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:04:30 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:05:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:05:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:40 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:24 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:06:07 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:15:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:42 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:00:22 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:02:00 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:44 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:30 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:13 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:00:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:02:30 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:07:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:09:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:03 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:05:14 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:59 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-14 18:02:27 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-14 18:00:10 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-02-14 18:02:55 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-02-14 18:02:43 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-02-14 17:00:48 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.087 |  |
| 2026-02-14 18:05:02 | Padiyathalawa (Maduru Oya) | 2.67 | 🟢 Normal | -0.421 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)