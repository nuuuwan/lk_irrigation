# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_07:02:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 07:02:00 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.013 |  |
| 2026-02-11 07:01:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:01:28 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-11 07:01:27 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.071 |  |
| 2026-02-11 07:00:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.107 |  |
| 2026-02-11 07:00:11 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-11 06:29:58 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.002 |  |
| 2026-02-11 06:16:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:14:38 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-02-11 06:12:11 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:10:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.071 |  |
| 2026-02-11 06:10:37 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:09:29 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-11 06:08:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.107 |  |
| 2026-02-11 06:07:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:07:45 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-11 06:07:35 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:07:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:06:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-02-11 06:06:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:06:08 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 06:03:17 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-11 06:07:45 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-11 07:00:11 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-11 06:01:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:01:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:12:11 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:05:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:03:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:02:06 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:01:51 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:04:28 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:07:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:07:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:01:15 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:03:12 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:05:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:06:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:10:37 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:07:35 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:16:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:01:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:06:08 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-11 06:01:02 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.002 |  |
| 2026-02-11 06:29:58 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.002 |  |
| 2026-02-11 06:05:49 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-11 07:01:28 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-11 06:06:30 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-02-11 06:01:12 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-02-11 07:02:00 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.013 |  |
| 2026-02-11 06:03:27 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-02-11 06:02:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-02-11 06:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-02-11 07:01:27 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.071 |  |
| 2026-02-11 07:00:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.107 |  |
| 2026-02-11 06:02:47 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.210 |  |
| 2026-02-11 06:04:03 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -2.261 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)