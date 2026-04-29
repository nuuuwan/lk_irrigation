# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_11:05:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 11:05:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:05:00 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:04:22 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-04-29 11:04:02 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:42 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:09 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:08 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.041 |  |
| 2026-04-29 11:02:55 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-29 11:02:53 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:02:50 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:02:42 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-04-29 11:02:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:02:33 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-29 11:02:26 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-29 11:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:02:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:40 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:01:32 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:28 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:01:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:20 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:00:31 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 11:00:28 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:00:22 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-29 11:00:10 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-29 10:39:03 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-04-29 10:24:58 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 10:21:29 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 10:14:21 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 11:02:42 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-04-29 10:03:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-29 11:02:55 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-29 11:02:33 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-29 11:00:31 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 10:01:42 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 11:02:53 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:01:40 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:05:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 11:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:02:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 10:02:52 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:02:40 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:04:02 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:32 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:01:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:42 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:05:00 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:03:09 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:00:28 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 11:04:22 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-04-29 10:01:49 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-29 10:06:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-29 11:00:22 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-29 10:05:27 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.014 |  |
| 2026-04-29 10:07:21 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-04-29 11:01:28 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:02:50 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:01:20 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:00:10 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-29 11:02:26 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-29 10:00:59 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-04-29 10:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.031 |  |
| 2026-04-29 10:39:03 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-04-29 11:03:08 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.041 |  |
| 2026-04-29 10:06:34 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)