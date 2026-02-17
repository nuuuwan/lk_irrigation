# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_18:19:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 18:19:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:19:15 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.008 |  |
| 2026-02-17 18:11:24 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:09:26 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.022 |  |
| 2026-02-17 18:09:09 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:07:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-02-17 18:07:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 18:06:25 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:06:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:05:37 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-02-17 18:05:32 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:05:02 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-17 18:05:01 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:53 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-17 18:03:50 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:45 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:35 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.135 |  |
| 2026-02-17 18:02:57 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:48 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:35 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:32 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-17 18:02:32 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-02-17 18:01:59 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:48 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.112 |  |
| 2026-02-17 18:01:47 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.041 |  |
| 2026-02-17 18:01:40 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:40 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.058 |  |
| 2026-02-17 18:01:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:16 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-17 18:01:11 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:07 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 18:02:32 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-17 18:01:16 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-17 18:07:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 18:04:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 18:01:11 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:00:34 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:59 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:57 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:50 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:09:09 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:40 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:01:07 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:35 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:05:01 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:48 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:03:45 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:11:24 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:19:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:35 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:19:15 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.008 |  |
| 2026-02-17 18:06:25 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:04:53 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:05:32 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-02-17 18:05:02 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-17 18:02:32 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-17 18:05:37 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-02-17 18:09:26 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.022 |  |
| 2026-02-17 18:07:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-02-17 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.040 |  |
| 2026-02-17 18:01:47 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.041 |  |
| 2026-02-17 18:01:40 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.058 |  |
| 2026-02-17 18:01:48 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.112 |  |
| 2026-02-17 18:03:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)