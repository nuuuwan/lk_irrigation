# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_08:07:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 08:07:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:33 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.037 |  |
| 2026-06-02 08:07:27 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:08 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:05 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.312 |  |
| 2026-06-02 08:06:55 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.028 |  |
| 2026-06-02 08:06:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.048 |  |
| 2026-06-02 08:06:11 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.092 |  |
| 2026-06-02 08:06:09 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:04:48 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:04:08 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:04:01 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:47 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:47 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-06-02 08:03:34 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:28 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:27 | Manampitiya (Mahaweli Ganga) | -0.91 | 🟢 Normal | -5.571 |  |
| 2026-06-02 08:03:25 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:03:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:50 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-06-02 08:02:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:30 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:02:03 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:52 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:37 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:23 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:02 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:00:31 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-02 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.071 |  |
| 2026-06-02 08:00:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:53:39 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -5.571 |  |
| 2026-06-02 07:29:49 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:28:56 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:28:38 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:28:37 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:19:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 08:00:31 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-02 08:03:28 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:00:11 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:30:16 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 06:00:28 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:52 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:06:35 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:08 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:04:01 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:37 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:39 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:29:49 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:03 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:23 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:34 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:30 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:04:08 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 07:05:03 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:01:02 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:06:09 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:03:47 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:02:50 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:07:27 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-02 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:02:04 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:03:25 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-02 08:03:47 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-06-02 08:06:55 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.028 |  |
| 2026-06-02 08:07:33 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.037 |  |
| 2026-06-02 07:02:55 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-06-02 08:06:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.048 |  |
| 2026-06-02 08:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-06-02 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.071 |  |
| 2026-06-02 08:06:11 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.092 |  |
| 2026-06-02 08:07:05 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.312 |  |
| 2026-06-02 08:03:27 | Manampitiya (Mahaweli Ganga) | -0.91 | 🟢 Normal | -5.571 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)