# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_09:18:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 09:18:02 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:13:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-30 09:12:48 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-30 09:11:14 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.027 |  |
| 2026-04-30 09:10:46 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:08:28 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.063 |  |
| 2026-04-30 09:08:05 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:08:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.057 |  |
| 2026-04-30 09:05:18 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.230 |  |
| 2026-04-30 09:04:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-30 09:04:08 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-30 09:03:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:31 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-30 09:03:20 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:14 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:03:10 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:09 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.020 |  |
| 2026-04-30 09:03:05 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-04-30 09:02:59 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:02:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:02:45 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-04-30 09:02:37 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-30 09:02:34 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-30 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:02:20 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:01:48 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-04-30 09:01:40 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:01:29 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:01:28 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-30 09:01:26 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:01:22 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 09:01:15 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:01:11 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 09:00:44 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.054 |  |
| 2026-04-30 09:00:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 09:00:09 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 09:02:37 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-30 09:13:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-30 09:00:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 09:02:34 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-30 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 09:04:08 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-30 09:01:22 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 09:00:09 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:03:14 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:01:11 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:08:05 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 09:02:59 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:10 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:24 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:13:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:01:26 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:10:46 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:02:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:18:02 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:03:20 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:01:15 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:02:20 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 09:04:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-30 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:01:29 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:01:40 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 09:03:09 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.020 |  |
| 2026-04-30 09:03:31 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-30 09:01:48 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-04-30 09:11:14 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.027 |  |
| 2026-04-30 09:12:48 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.029 |  |
| 2026-04-30 09:01:28 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-30 09:03:05 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-04-30 09:02:45 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-04-30 09:00:44 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.054 |  |
| 2026-04-30 09:08:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.057 |  |
| 2026-04-30 09:08:28 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.063 |  |
| 2026-04-30 09:05:18 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)