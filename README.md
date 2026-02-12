# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_08:06:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,856 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 08:06:32 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.067 |  |
| 2026-02-12 08:06:22 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:05:55 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:05:43 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:05:36 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:05:22 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 08:04:44 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:19 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:13 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-12 08:04:12 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:03:49 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.084 |  |
| 2026-02-12 08:03:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-12 08:03:29 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 08:03:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-12 08:03:17 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:03:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 08:03:07 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.071 |  |
| 2026-02-12 08:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 08:02:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:02:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-02-12 08:02:22 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:02:21 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.058 |  |
| 2026-02-12 08:02:13 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-12 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:02:04 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:01:55 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:50 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:46 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:37 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:22:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:20:46 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.058 |  |
| 2026-02-12 07:17:53 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-02-12 07:15:48 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:14:22 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:14:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:13:13 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:11:33 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 08:03:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-12 08:04:13 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-12 08:03:10 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 08:05:22 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-12 08:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 08:03:29 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 07:03:10 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 06:04:33 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 08:01:46 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:55 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:03:17 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:37 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:11:33 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:15:48 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:44 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:06:22 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:22:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:19 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:01:50 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:05:36 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:05:55 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:12 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:14:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:02:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 07:09:10 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-02-12 08:02:22 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:05:43 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:02:04 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-12 08:03:39 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-12 08:02:13 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-12 07:17:53 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-02-12 08:02:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-02-12 08:02:21 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.058 |  |
| 2026-02-12 07:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.063 |  |
| 2026-02-12 08:06:32 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.067 |  |
| 2026-02-12 08:03:07 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.071 |  |
| 2026-02-12 08:03:49 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)