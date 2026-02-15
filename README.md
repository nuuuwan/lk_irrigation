# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_04:28:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 04:28:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.050 |  |
| 2026-02-16 04:26:41 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-02-16 04:17:53 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:17:41 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:17:11 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:13:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-16 04:11:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:07:35 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.005 |  |
| 2026-02-16 04:06:33 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-02-16 04:06:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:06:18 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-02-16 04:06:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.004 |  |
| 2026-02-16 04:06:08 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-16 04:06:03 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:05:53 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-16 04:05:42 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:05:21 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:04:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:04:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 04:04:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-16 04:04:03 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:03:06 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:02:29 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-02-16 04:02:15 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:01:59 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:01:20 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.056 |  |
| 2026-02-16 04:01:20 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.582 |  |
| 2026-02-16 04:01:12 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-16 04:01:03 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-02-16 04:00:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.022 |  |
| 2026-02-16 04:00:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.097 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 04:06:33 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-02-16 04:06:08 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-16 04:00:23 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-16 03:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-16 04:04:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 04:13:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-16 04:07:35 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.005 |  |
| 2026-02-16 04:06:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.004 |  |
| 2026-02-16 04:01:20 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:05:42 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:02:15 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:03:06 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 03:02:54 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 03:01:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:06:03 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:17:41 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:11:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:06:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:04:03 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-16 03:03:28 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:05:21 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:04:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 03:06:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:17:53 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:10 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 04:01:03 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-02-16 04:04:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-16 04:02:29 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-02-16 04:06:18 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-02-16 04:26:41 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-02-16 04:01:12 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-16 04:00:50 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.022 |  |
| 2026-02-16 04:05:53 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-16 04:28:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.050 |  |
| 2026-02-16 04:01:20 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.056 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-16 04:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.582 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)