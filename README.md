# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_04:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 04:03:25 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-11 04:02:56 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 04:02:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:46 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:28 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-06-11 04:02:28 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 04:02:24 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-06-11 04:01:45 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.034 |  |
| 2026-06-11 04:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:00:53 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:00:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 04:00:20 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:33:57 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-11 03:28:46 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:26:14 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:24:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-06-11 03:23:30 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 03:05:59 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 1.125 | 🔺 Rising |
| 2026-06-11 03:33:57 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-11 04:03:25 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-11 03:11:12 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 03:06:09 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 03:08:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 04:00:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 03:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 03:05:21 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 04:02:28 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 03:06:35 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 04:02:56 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 01:26:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.004 |  |
| 2026-06-11 03:04:08 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:00:20 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:00:53 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 02:03:42 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:46 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:04:15 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:26:14 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:28:46 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:01:50 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:02:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:02:24 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:09:11 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 03:03:03 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-06-11 04:02:28 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-06-11 03:23:30 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.016 |  |
| 2026-06-11 02:05:54 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-11 03:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-11 03:24:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-06-11 04:01:45 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.034 |  |
| 2026-06-11 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-06-11 03:11:58 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)