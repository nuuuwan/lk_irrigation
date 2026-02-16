# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_05:09:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,197 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 05:09:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-17 05:06:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:06:16 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |
| 2026-02-17 05:05:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:30 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-17 05:05:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:18 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-17 05:05:00 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:04:49 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:04:39 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.486 |  |
| 2026-02-17 05:04:22 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-17 05:04:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:28 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:02:54 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-17 05:02:38 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -3.130 |  |
| 2026-02-17 05:02:18 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 05:02:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -3.130 |  |
| 2026-02-17 05:02:13 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-17 05:02:05 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -72.000 |  |
| 2026-02-17 05:02:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:02:04 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -72.000 |  |
| 2026-02-17 05:02:03 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -72.000 |  |
| 2026-02-17 05:02:02 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -72.000 |  |
| 2026-02-17 05:02:00 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -72.000 |  |
| 2026-02-17 05:02:00 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-17 05:02:00 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:01:36 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:01:30 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-02-17 05:00:47 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-02-17 05:00:30 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-17 04:59:42 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:48:35 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:41:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.032 |  |
| 2026-02-17 04:41:45 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 05:04:22 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-17 05:02:00 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-17 05:05:30 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-17 05:02:18 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 05:02:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:59:42 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:01:41 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:02:00 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:05:56 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:03:19 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:28 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:05:06 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:00 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:03:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:06:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:48:35 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 04:05:02 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:04:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 03:02:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:04:49 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-17 05:05:18 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-17 05:02:54 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-17 05:09:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-17 03:02:00 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-17 05:02:13 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-17 05:00:30 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-17 05:00:47 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-02-17 05:01:30 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-02-17 05:06:16 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |
| 2026-02-16 18:00:50 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |
| 2026-02-17 05:04:39 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.486 |  |
| 2026-02-17 05:02:38 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -3.130 |  |
| 2026-02-17 05:02:05 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)