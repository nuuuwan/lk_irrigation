# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_10:26:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 10:26:44 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:17:05 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.046 |  |
| 2026-02-04 10:13:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:12:03 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:11:46 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.026 |  |
| 2026-02-04 10:09:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:09:30 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:06:15 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:06:12 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.061 |  |
| 2026-02-04 10:06:08 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-02-04 10:05:54 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-04 10:05:11 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-02-04 10:04:12 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:52 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:45 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:36 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:23 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-04 10:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:38 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:37 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:29 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:18 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.211 |  |
| 2026-02-04 10:02:10 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:01:38 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-02-04 10:01:13 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-04 10:00:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:53:25 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.095 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 10:01:13 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:29 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:06:15 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:09:30 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:10 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:45 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:36 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:00:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:12:03 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:52 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:37 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:09:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:03:23 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:26:44 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:13:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:04:12 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:02:38 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 10:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-04 10:01:38 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34⌛ | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-04 10:11:46 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.026 |  |
| 2026-02-04 10:05:54 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-04 10:05:11 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-02-04 10:06:08 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-02-04 10:17:05 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.046 |  |
| 2026-02-04 10:06:12 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-04 09:53:25 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.095 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-04 10:02:18 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)