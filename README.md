# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_08:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,975 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 08:06:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-04-11 08:05:52 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-11 08:05:25 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:05:19 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:05:16 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-11 08:05:11 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-04-11 08:04:48 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:46 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.048 |  |
| 2026-04-11 08:04:41 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:32 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:23 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-04-11 08:03:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-04-11 08:02:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.050 |  |
| 2026-04-11 08:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 08:02:13 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.031 |  |
| 2026-04-11 08:02:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:58 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-04-11 08:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-11 08:01:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:28 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:22 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 08:01:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:07 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-04-11 08:00:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:22:41 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:21:27 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:17:21 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 08:01:07 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-04-11 07:01:03 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-11 08:05:16 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-11 07:09:41 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-11 07:07:09 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-11 08:01:22 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 08:02:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:00:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:01:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:05:19 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:01:42 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:06:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:03:32 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:28 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:22:41 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:04:29 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:41 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:05:25 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 07:21:27 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:01:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:04:48 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-11 08:05:11 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-04-11 07:05:16 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-11 08:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-11 08:01:58 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-04-11 08:03:23 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-04-11 08:05:52 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-11 08:03:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-04-11 08:02:13 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.031 |  |
| 2026-04-11 07:08:34 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.036 |  |
| 2026-04-11 08:04:46 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.048 |  |
| 2026-04-11 08:02:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.050 |  |
| 2026-04-11 08:06:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)