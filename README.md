# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_09:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 09:08:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:08:10 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:07:01 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:06:53 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-02-12 09:06:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:06:11 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:05:49 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:05:40 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-12 09:05:35 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.081 |  |
| 2026-02-12 09:05:34 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:05:05 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.146 |  |
| 2026-02-12 09:04:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-12 09:04:11 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.035 |  |
| 2026-02-12 09:03:49 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.089 |  |
| 2026-02-12 09:03:37 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 09:03:25 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-02-12 09:03:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:10 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-02-12 09:03:07 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 09:02:27 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:15 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:15 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:15 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:12 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:10 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:05 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:30 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-02-12 09:01:25 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.020 |  |
| 2026-02-12 09:01:25 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:06 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:00:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 08:37:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:24:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:24:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:21:30 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:21:24 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:18:38 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:16:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-02-12 08:12:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 09:03:37 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 09:02:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 09:00:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 09:02:10 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:04:11 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:25 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:27 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:07 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:08:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:12 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:18:38 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:21:30 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:15 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:05:34 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:06:22 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:04:19 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:01:06 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:15 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:03:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:06:11 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:07:01 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:02:05 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:06:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 08:24:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:05:49 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:08:10 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-12 09:04:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-12 09:01:30 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-02-12 09:03:25 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-02-12 08:16:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-02-12 09:06:53 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-02-12 09:05:40 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-12 09:01:25 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.020 |  |
| 2026-02-12 09:03:10 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-02-12 09:03:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.035 |  |
| 2026-02-12 09:05:35 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.081 |  |
| 2026-02-12 09:03:49 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.089 |  |
| 2026-02-12 09:05:05 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)