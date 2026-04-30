# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_08:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,923 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 08:18:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-04-30 08:17:20 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:15:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:13:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:13:08 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.005 |  |
| 2026-04-30 08:12:29 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:10:45 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-04-30 08:08:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.072 |  |
| 2026-04-30 08:07:05 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-04-30 08:06:10 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 08:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.073 |  |
| 2026-04-30 08:05:22 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.041 |  |
| 2026-04-30 08:04:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:04:29 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.029 |  |
| 2026-04-30 08:03:46 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 08:03:30 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-30 08:03:17 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:03:09 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 08:02:56 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-04-30 08:02:53 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-30 08:02:52 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:02:38 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-04-30 08:02:28 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 08:02:23 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-04-30 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.021 |  |
| 2026-04-30 08:02:19 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:02:18 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.080 |  |
| 2026-04-30 08:02:15 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-30 08:02:12 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:34 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:01:24 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:01:19 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-04-30 08:01:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 08:01:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.125 |  |
| 2026-04-30 08:01:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:00:47 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 08:00:41 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 08:02:53 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-30 08:02:28 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 08:00:47 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-30 08:03:09 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 08:06:10 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 08:01:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 08:03:46 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 08:15:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:24 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:03:17 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:34 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:13:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:01:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:04:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:17:20 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:02:19 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:02:12 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-30 08:13:08 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.005 |  |
| 2026-04-30 08:01:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:02:52 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-04-30 08:02:38 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-04-30 08:07:05 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-04-30 08:10:45 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-04-30 08:03:30 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-30 08:02:15 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-30 08:02:21 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.021 |  |
| 2026-04-30 08:18:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-04-30 08:04:29 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.029 |  |
| 2026-04-30 08:02:56 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-04-30 08:05:22 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.041 |  |
| 2026-04-30 08:01:19 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-04-30 08:00:41 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.052 |  |
| 2026-04-30 08:08:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.072 |  |
| 2026-04-30 08:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.073 |  |
| 2026-04-30 08:02:18 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.080 |  |
| 2026-04-30 08:02:23 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.090 |  |
| 2026-04-30 08:01:11 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)