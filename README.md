# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_12:14:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 12:14:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:10:07 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:09:52 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-12 12:07:57 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.019 |  |
| 2026-02-12 12:07:45 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.447 |  |
| 2026-02-12 12:07:31 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-02-12 12:07:23 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-02-12 12:06:55 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:06:12 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:05:50 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:05:13 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:05:04 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.447 |  |
| 2026-02-12 12:04:49 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:37 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:22 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:08 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:04:04 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:55 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-12 12:03:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:16 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-02-12 12:03:14 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:03:09 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-12 12:03:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:02:54 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:02:52 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:02:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-02-12 12:02:05 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:02:02 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:59 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:46 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-12 12:01:45 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:45 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 12:01:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:39 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:37 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:01:14 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 12:00:18 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 12:09:52 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-12 12:01:14 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 12:01:46 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-12 12:01:45 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 12:02:01 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:59 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:45 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:22 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:06:12 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:02:52 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:49 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:06:55 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:10:07 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:05:50 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:05:13 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:01:39 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:04 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:33 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:04:37 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:00:18 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:14:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:02:54 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 12:03:09 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:02:02 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:02:05 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:03:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:04:08 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:01:37 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-12 12:03:16 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-02-12 12:03:55 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-12 12:07:23 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-02-12 12:07:57 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.019 |  |
| 2026-02-12 12:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-12 12:02:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-02-12 12:07:31 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-02-12 12:07:45 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.447 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)