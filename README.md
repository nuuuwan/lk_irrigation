# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_15:06:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 15:06:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-04 15:06:24 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:06:00 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-04 15:05:16 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:05:08 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:04:40 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-04 15:04:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 15:03:47 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.706 |  |
| 2026-02-04 15:03:39 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.013 |  |
| 2026-02-04 15:03:26 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:25 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-02-04 15:03:19 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.035 |  |
| 2026-02-04 15:03:14 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:03:10 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-04 15:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-04 15:03:07 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 15:02:48 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:45 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-04 15:02:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:37 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-02-04 15:02:35 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:01:15 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:01:09 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-04 15:01:05 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-02-04 15:00:53 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:00:32 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 15:06:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-04 15:02:43 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 15:03:10 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-04 15:06:00 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-04 15:04:40 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-04 15:03:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 15:03:07 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 15:02:48 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:37 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:45 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:05:08 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:01:15 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:04:09 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:41 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:06:24 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:03:26 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 15:02:35 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 15:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-04 15:01:09 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-04 15:01:05 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-02-04 15:03:39 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.013 |  |
| 2026-02-04 15:00:53 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:05:16 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-02-04 15:03:14 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-04 15:00:32 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-02-04 15:03:25 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-02-04 15:03:19 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.035 |  |
| 2026-02-04 15:02:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-04 15:03:47 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.706 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)