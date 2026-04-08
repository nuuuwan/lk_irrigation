# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_18:23:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,728 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 18:23:20 | Panadugama (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.008 |  |
| 2026-04-08 18:12:52 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-04-08 18:12:48 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:12:45 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:12:42 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:10:26 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:08:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.056 |  |
| 2026-04-08 18:07:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 18:06:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:06:22 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.037 |  |
| 2026-04-08 18:05:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:05:41 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:05:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-08 18:04:54 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:04:46 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-08 18:04:33 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:03:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:03:13 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 18:03:13 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:03:13 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:03:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:03:01 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-08 18:02:52 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:29 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:02:23 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:02:16 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 18:02:15 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-04-08 18:01:43 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:38 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:19 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-08 18:01:19 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:00:44 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-08 18:00:36 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.071 |  |
| 2026-04-08 18:00:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 17:53:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-08 18:04:46 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-08 18:03:01 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-08 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-08 18:02:16 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 18:07:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 18:03:13 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 18:00:44 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:19 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-08 17:01:46 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:23 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:10:26 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:03:13 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:12:48 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:06:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:05:41 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:43 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:01:38 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:05:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:00:08 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:03:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:23:20 | Panadugama (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.008 |  |
| 2026-04-08 17:03:53 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:05:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:02:29 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:03:13 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:04:33 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:03:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:01:19 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-08 18:02:52 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-04-08 17:53:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.025 |  |
| 2026-04-08 18:12:52 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-04-08 18:02:15 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-04-08 18:06:22 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.037 |  |
| 2026-04-08 18:08:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.056 |  |
| 2026-04-08 18:00:36 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)