# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_15:17:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 15:17:26 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:10:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-26 15:09:27 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-26 15:09:01 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-02-26 15:06:27 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-02-26 15:06:03 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:05:06 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.058 |  |
| 2026-02-26 15:04:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:04:01 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:31 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:03:11 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:58 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:57 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:29 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:20 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:11 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:09 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.041 |  |
| 2026-02-26 15:02:08 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:02 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.014 |  |
| 2026-02-26 15:02:01 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:54 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:51 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:46 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-02-26 15:01:33 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:30 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:01:30 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:29 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:01:26 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:01:19 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:00:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:00:19 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.195 |  |
| 2026-02-26 15:00:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 15:10:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-26 13:03:47 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-26 15:09:27 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-26 15:02:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:33 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:19 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:20 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:11 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:57 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:54 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:01 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:30 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:06:03 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:58 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:04:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:29 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:04:01 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:17:26 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:01:51 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:03:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:08 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 15:09:01 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-02-26 15:01:26 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:03:31 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:01:29 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:01:30 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:00:25 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-26 15:00:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-02-26 15:06:27 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-02-26 15:02:02 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.014 |  |
| 2026-02-26 15:01:46 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-02-26 15:02:09 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.041 |  |
| 2026-02-26 15:05:06 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.058 |  |
| 2026-02-26 15:00:19 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)