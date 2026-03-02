# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_12:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 12:03:50 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-02 12:03:43 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 12:03:22 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:03:22 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 12:03:19 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:53 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-02 12:02:51 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-02 12:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:47 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-03-02 12:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:18 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-03-02 12:02:12 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.097 |  |
| 2026-03-02 12:02:07 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:02:05 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.012 |  |
| 2026-03-02 12:01:33 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 12:01:20 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:01:15 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:00:27 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:00:19 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:00:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:53:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-03-02 11:26:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:13:03 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-03-02 11:09:59 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:09:04 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 11:53:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-03-02 11:01:14 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-02 11:01:18 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-02 11:03:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-02 12:02:53 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-02 12:01:33 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 12:02:51 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-02 12:03:22 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 12:03:43 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 12:03:19 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:00:27 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:04:08 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:00:19 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:04:14 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:01:18 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:06:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:07:08 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:26:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:00:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:08:19 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:09:04 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:05:32 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:03:50 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-02 12:02:07 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:03:22 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:01:20 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:02:47 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-03-02 12:01:15 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-02 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-02 12:02:05 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.012 |  |
| 2026-03-02 11:03:15 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-03-02 11:02:31 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.014 |  |
| 2026-03-02 11:00:54 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-02 12:02:18 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-03-02 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-03-02 11:05:09 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.039 |  |
| 2026-03-02 12:02:12 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)