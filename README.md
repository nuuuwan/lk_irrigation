# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_03:06:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,353 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 03:06:48 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -504.000 |  |
| 2026-02-15 03:06:47 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -504.000 |  |
| 2026-02-15 03:06:45 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -504.000 |  |
| 2026-02-15 03:06:33 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:06:31 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:06:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:05:46 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:05:39 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 03:05:08 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-02-15 03:05:08 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-02-15 03:04:47 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-15 03:04:12 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:04:07 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 03:03:55 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:03:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 5.225 | 🔺 Rising |
| 2026-02-15 03:03:49 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-15 03:03:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 5.225 | 🔺 Rising |
| 2026-02-15 03:03:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 5.225 | 🔺 Rising |
| 2026-02-15 03:03:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-15 03:03:11 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:03:02 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:54 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:46 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-15 03:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:31 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 03:02:28 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:22 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 03:02:07 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:01:57 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-02-15 03:01:31 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 03:01:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:00:28 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 03:00:09 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.024 |  |
| 2026-02-15 02:22:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.003 |  |
| 2026-02-15 02:12:46 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 03:03:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 5.225 | 🔺 Rising |
| 2026-02-15 00:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-15 00:00:48 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-15 03:02:46 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-15 03:03:49 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-15 03:01:31 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 03:02:22 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-15 03:02:31 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 03:05:39 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 03:04:07 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 03:00:28 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:04:13 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 22:00:48 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 03:03:55 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:05:46 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:28 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:03:02 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:06:33 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:03:11 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:04:12 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:02:54 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:01:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:15 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 03:06:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:22:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.003 |  |
| 2026-02-15 02:07:01 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.005 |  |
| 2026-02-15 03:05:08 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-02-15 03:03:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-15 03:05:08 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-02-15 03:04:47 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-15 03:00:09 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.024 |  |
| 2026-02-15 03:01:57 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-02-15 02:01:13 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.090 |  |
| 2026-02-15 03:06:48 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -504.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)