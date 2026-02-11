# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_08:06:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,964 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 08:06:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:26 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:05:57 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:05:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:05:21 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.040 |  |
| 2026-02-11 08:05:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:04:52 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:04:39 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.056 |  |
| 2026-02-11 08:04:23 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:04:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:35 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:30 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:30 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:07 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:00 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:02:49 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.033 |  |
| 2026-02-11 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.050 |  |
| 2026-02-11 08:02:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:02:12 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:02:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.059 |  |
| 2026-02-11 08:01:59 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:59 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:57 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:01:45 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:01:25 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:23 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.057 |  |
| 2026-02-11 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:39:13 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:22:49 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:20:56 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.023 |  |
| 2026-02-11 07:16:05 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:15:15 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:10:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 08:03:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:45 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:57 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:30 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:03:54 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:30 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:05:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:26 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:02:12 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:07 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:25 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:04:23 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:35 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:04:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:59 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:04:52 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:28 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:01:59 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:06:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:05:57 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:39:13 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:02:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-11 07:06:50 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-11 08:03:00 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:05:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:01:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-02-11 08:01:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-11 07:20:56 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.023 |  |
| 2026-02-11 06:02:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-02-11 08:02:49 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.033 |  |
| 2026-02-11 08:05:21 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.040 |  |
| 2026-02-11 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.050 |  |
| 2026-02-11 08:04:39 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.056 |  |
| 2026-02-11 08:01:23 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.057 |  |
| 2026-02-11 08:02:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.059 |  |
| 2026-02-11 07:01:27 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)